# Author: Adam Bujak
# Date Created: Saturday, September 28, 2019
# Description: DCM User Account Manager Source File
# Filename: duam.py

from src.dcm_constants                  import *
from DCMDatabase.dbpm                   import *
from enum                               import Enum
from DCMUserAccountManager.frangeFunc   import *
import hashlib, binascii, os


#############################################################
####################### Sessions Enum #######################
#############################################################


class FailureCodes(Enum):
    SUCCESS                 = 0
    INCORRECT_PASSWORD      = 1
    INCORRECT_USERNAME      = 2
    EXISTING_USER           = 3
    INVALID_CREDENTIALS     = 4
    MISSING_PERMISSIONS     = 5
    TOO_MANY_USERS          = 6
    INVALID_USER_INPUT      = 7
    INVALID_RATE_INPUT      = 8
    INVALID_ATRIUM_INPUT    = 9
    INVALID_VENTRICLE_INPUT = 10

class SessionStates(Enum):
    LOGGED_OUT  = 0
    LOGGED_IN   = 1

class UserRole(Enum):
    ADMIN       = 0
    USER        = 1

class LoginData:
    def __init__(self, p_username, p_password):
        self.username = p_username
        self.password = p_password

class UserInputProgramData:
    def __init__(self, p_lowerRateLimit, p_upperRateLimit, 
        p_atrialAmplitude, p_atrialPulseWidth, p_atrialSensingThreshold, p_atrialRefractoryPeriod, 
        p_ventricularAmplitude, p_ventricularPulseWidth, p_ventricularSensingThreshold, p_ventricularRefractoryPeriod):
        self.lowerRateLimit               = p_lowerRateLimit
        self.upperRateLimit               = p_upperRateLimit
        self.atrialAmplitude              = p_atrialAmplitude
        self.atrialPulseWidth             = p_atrialPulseWidth
        self.atrialSensingThreshold       = p_atrialSensingThreshold
        self.atrialRefractoryPeriod       = p_atrialRefractoryPeriod
        self.ventricularAmplitude         = p_ventricularAmplitude
        self.ventricularPulseWidth        = p_ventricularPulseWidth
        self.ventricularSensingThreshold  = p_ventricularSensingThreshold
        self.ventricularRefractoryPeriod  = p_ventricularRefractoryPeriod



#############################################################
################ User Account Manager Class #################
#############################################################


class DUAM:

    def __init__(self):
        """Initialize User Account Manager"""
        # Start Database Manager #
        self.dbManager = DBPM()
        self.user      = None
        self.state     = SessionStates.LOGGED_OUT

        # Make admin user - this is only needed when database is empty,
        # and admin user has never been created yet 
        self.p_makeAdminUser();

    def getSessionState(self):
        return self.state

    def signInUser(self, p_loginData):
        """Signs user in.
        p_password must not be hashed,
        returns FailureCode
        """
        username = p_loginData.username
        password = p_loginData.password

        # Check user to make sure it exists
        if (self.dbManager.userExists(username)):

            # Get user data from database
            userData = self.dbManager.getUserData(username)
            # Check if password is correct
            passwordValid = verify_password(userData.getPassword(), password)
            # Redundant check to make sure correct user data is being returned
            usernameValid = (userData.getUsername() == username)
            #debugging----------------------------
            print("usernameValid:", usernameValid)
            print("passwordValid:", passwordValid)
            if passwordValid and usernameValid:
                self.user = userData
                self.state = SessionStates.LOGGED_IN
                return FailureCodes.SUCCESS

        return FailureCodes.INVALID_CREDENTIALS

    def signOut(self):
        '''Signs user out
        '''
        self.user = None
        self.state = SessionStates.LOGGED_OUT
        return True
        
    def p_makeAdminUser(self):
        """Adds admin to database if not already there
        """

        # If already in database, return
        if self.dbManager.userExists(C_ADMINISTRATOR_USERNAME):
            return
        # Store admin in database
        self.dbManager.createUser(C_ADMINISTRATOR_USERNAME, C_ADMINISTRATOR_PASSWORD, UserRole.ADMIN, UserProgramData(1,2,3,4,5,6,7,8,9,10))

    def makeNewUser(self, p_loginData, p_adminPassword):
        """Adds new user to database.
        p_password must not be hashed,
        returns FailureCode
        """
        if not self.validNewUserInput(p_loginData.username, p_loginData.password):
            return FailureCodes.INVALID_USER_INPUT

        p_username = p_loginData.username
        p_password = hash_password(p_loginData.password)
        p_adminPassword = hash_password(p_adminPassword)
        if self.validUser():
            return FailureCodes.MISSING_PERMISSIONS
        if not self.validNumUsers():
            return FailureCodes.TOO_MANY_USERS


        # This will enforce only Admin can create users, Currently anyone can create user
        # # If current user's role isn't admin, return 
        # if self.user.getRole() != UserRole.ADMIN:
        #     return FailureCodes.MISSING_PERMISSIONS

        # # If current user isn't admin, return 
        # if self.user.getUsername() != C_ADMINISTRATOR_USERNAME:
        #     return FailureCodes.MISSING_PERMISSIONS
        
        # # Verify administrator password
        # if not verify_password(self.user.getPassword(), p_adminPassword):
        #     return FailureCodes.INVALID_CREDENTIALS

        # If user already exists, return False
        if self.dbManager.userExists(p_username):
            return FailureCodes.EXISTING_USER

        # Store user in database
        self.dbManager.createUser(p_username, p_password, UserRole.USER, UserProgramData(1,2,3,4,5,6,7,8,9,10))
        return FailureCodes.SUCCESS

    def changeUserPassword(self, p_username, p_existingPassword, p_newPassword):
        """Changes user's password.
        Both password parameters must not be hashed,
        returns FailureCode
        """
        p_existingPassword = hash_password(p_existingPassword)
        p_newPassword      = hash_password(p_newPassword)

        # If username doesn't exist
        if not self.dbManager.userExists(p_username):
            return FailureCodes.INVALID_CREDENTIALS

        user = self.dbManager.getUserData(p_username)

        # Verify user password
        if not verify_password(user.getPassword(), p_existingPassword):
            return FailureCodes.INVALID_CREDENTIALS

        self.changeUserPassword(p_username, p_newPassword)
        return FailureCodes.SUCCESS

    def validUser(self):
        """ Checks if current user is valid,
        if signed out, it returns False,
        if user object is None it returns False
        """
        if self.state == SessionStates.LOGGED_OUT:
            return False

        # if self.user == None:
        #     return False
        return True

    def validNewUserInput(self, username, password):
        if len(username) < 4 or len(password) < 4:
            return False
        return True



    def validRateLims(self, p_upperRateLim, p_lowerRateLim):
        """Validates users input for rate limits
        """
        checks = 0;
        #check p_lowerRateLim
        for valid in frange(30,50,5):
            if p_lowerRateLim == valid:
                checks += 1;
                break
        for valid in frange(51,90,1):
            if p_lowerRateLim == valid:
                checks += 1;
                break
        for valid in frange(95,175,5):
            if p_lowerRateLim == valid:
                checks += 1;
                break
        #check p_upperRateLim
        for valid in frange(50,175,5):
            if p_upperRateLim == valid and p_upperRateLim >= p_lowerRateLim:
                checks += 1;
                break
        if checks == 2:
            return True
        return False

    def validChamberPara(self, p_pulseAmp, p_pulseWidth, p_sensThres, p_refracPeriod):
        """Validates users input for chamber's arguments
        """
        checks = 0;
        #check p_pulseAmp
        for valid in frange(0.5,3.2,0.1):
            if p_pulseAmp == valid:
                checks += 1;
                break
        for valid in frange(3.5,7.0,0.5):
            if p_pulseAmp == valid:
                checks += 1;
                break
        #check p_pulseWidth
        if p_pulseWidth == 0.05:
            checks += 1;
        for valid in frange(0.1,1.9,0.1):
            if p_pulseWidth == valid:
                checks += 1;
                break
        #check p_sensThres
        for valid in [0.25,0.5,0.75]:
            if p_sensThres == valid:
                checks += 1;
                break
        for valid in frange(1,10,0.5):
            if p_sensThres == valid:
                checks += 1;
                break
        #check p_refracPeriod
        for valid in frange(150,500,10):
            if p_refracPeriod == valid:
                checks += 1;
                break
        if checks == 4: #all four arguments are valid
            return True
        return False


    def validNumUsers(self):
        if self.dbManager.getNumUsers() >= 10:
            return False
        return True

    def programRateLim(self, p_upperRateLim, p_lowerRateLim):
        """Sets current user's upper and lower rate limits in database
        """
        if not self.validRateLims(p_upperRateLim, p_lowerRateLim):
            print('User imputted invalid rate parameter')
            return FailureCodes.INVALID_RATE_INPUT
        self.user.data.setUpperRateLimit(p_upperRateLim)
        self.user.data.setLowerRateLimit(p_lowerRateLim)
        return FailureCodes.SUCCESS



    def programAtriaPara(self, p_atriumAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod):
        """Sets current user's atrium data in database
        """
        if not self.validChamberPara(p_atriumAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod):
            print('User imputted invalid atruim parameter')
            return FailureCodes.INVALID_ATRIUM_INPUT
        self.user.data.setAtrialAmplitude(p_atriumAmp)
        self.user.data.setAtrialPulseWidth(p_atriumPulseWidth)
        self.user.data.setAtrialSensingThreshold(p_atriumSensThres)
        self.user.data.setAtrialRefractoryPeriod(p_atriumRefracPeriod)
        return FailureCodes.SUCCESS

        

    def programVentriclePara(self, p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
        """Sets current user's ventricle data in database
        """
        if not self.validChamberPara(p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
            print('User imputted invalid ventricle parameter')
            return FailureCodes.INVALID_VENTRICLE_INPUT
        self.user.data.setVentricularAmplitude(p_ventriclePulseAmp)
        self.user.data.setVentricularPulseWidth(p_ventriclePulseWidth)
        self.user.data.setVentricularSensingThreshold(p_ventricleSensThres)
        self.user.data.setVentricularRefractoryPeriod(p_ventricleRefracPeriod)
        return FailureCodes.SUCCESS



#############################################################
################ Password Hashing Functions #################
#############################################################
 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

