# Author: Adam Bujak
# Date Created: Saturday, September 28, 2019
# Description: DCM User Account Manager Source File
# Filename: duam.py

from Common.failCodes                   import FailureCodes
from Common.datatypes                   import PacemakerParameterData
from enum                               import Enum
from src.dcm_constants                  import *
from DCMDatabase.dbpm                   import *
from DCMUserAccountManager.frangeFunc   import *
import hashlib, binascii, os


#############################################################
####################### Sessions Enum #######################
#############################################################

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

defaultPacemakerParameterData = PacemakerParameterData(
    C_DEFAULT_PROGRAM_MODE,
    C_DEFAULT_UPPER_RATE_LIMIT,
    C_DEFAULT_LOWER_RATE_LIMIT,
    C_DEFAULT_ATRIAL_AMPLITUDE,
    C_DEFAULT_ATRIAL_PULSE_WIDTH,
    C_DEFAULT_ATRIAL_SENSING_THRESHOLD,
    C_DEFAULT_ATRIAL_REFRACTORY_PERIOD,
    C_DEFAULT_VENTRICULAR_AMPLITUDE,
    C_DEFAULT_VENTRICULAR_PULSE_WIDTH,
    C_DEFAULT_VENTRICULAR_SENSING_THRESHOLD,
    C_DEFAULT_VENTRICULAR_REFRACTORY_PERIOD,
    C_DEFAULT_FIXED_AV_DELAY,
    C_DEFAULT_MODULATION_SENSITIVITY,
    C_DEFAULT_RATE_MODULATION)


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
            # print("usernameValid:", usernameValid)
            # print("passwordValid:", passwordValid)
            if passwordValid and usernameValid:
                self.user = userData
                self.state = SessionStates.LOGGED_IN
                return FailureCodes.VALID

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
        self.dbManager.createUser(C_ADMINISTRATOR_USERNAME, C_ADMINISTRATOR_PASSWORD, UserRole.ADMIN, defaultPacemakerParameterData)

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
        self.dbManager.createUser(p_username, p_password, UserRole.USER, defaultPacemakerParameterData)
        return FailureCodes.VALID

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
        return FailureCodes.VALID

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

    def validMisc(self, p_upperRateLim, p_lowerRateLim, p_fixedAVDelay, p_modulationSensitivity):
        """Validates users input for rate limits
        """
        checks = 0;
        for val in [p_upperRateLim, p_lowerRateLim, p_fixedAVDelay, p_modulationSensitivity]:
            print(val)
            if val is None:
                checks += 1;
        #check p_lowerRateLim
        if not (p_lowerRateLim is None):
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
        if not (p_upperRateLim is None):
            for valid in frange(50,175,5):
                if p_upperRateLim == valid: #and p_upperRateLim >= p_lowerRateLim: #need to implement
                    checks += 1;
                    break
        if not (p_modulationSensitivity is None):
            if p_modulationSensitivity > 0 and p_modulationSensitivity <= 16:
                if p_modulationSensitivity is int:
                    checks += 1;
        if not (p_fixedAVDelay is None):
            if p_fixedAVDelay == 150:
                checks += 1
        if checks == 4:
            return True
        return False

    def validChamberPara(self, p_pulseAmp, p_pulseWidth, p_sensThres, p_refracPeriod):
        """Validates users input for chamber's arguments
        """
        checks = 0;
        for val in [p_pulseAmp, p_pulseWidth, p_sensThres, p_refracPeriod]:
            if val is None:
                checks += 1
        #check p_pulseAmp
        if not (p_pulseAmp is None):
            for valid in frange(500,3200,100):
                if p_pulseAmp == valid:
                    checks += 1;
                    break
            for valid in frange(3500,7000,500):
                if p_pulseAmp == valid:
                    checks += 1;
                    break
        #check p_pulseWidth
        if not (p_pulseWidth is None):
            for valid in frange(1,20,1):
                if p_pulseWidth == valid:
                    checks += 1;
                    break
        #check p_sensThres
        if not (p_sensThres is None):
            for valid in frange(1000,3300,10):
                if p_sensThres == valid:
                    checks += 1;
                    break
        #check p_refracPeriod
        if not (p_refracPeriod is None):
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

    def controlProgramData(self, programmedData):
        #change all these to getUpperRateLimit() ...
        #change all private naming convention
        self.programProgramMode(programmedData.getProgramMode())
        stateRateLim = self.programMisc(programmedData.upperRateLimit, programmedData.lowerRateLimit, programmedData.fixedAVDelay,
                programmedData.modulationSensitivity, programmedData.rateModulation)
        stateChamber1Para = self.programAtriaPara(programmedData.atrialAmplitude, programmedData.atrialPulseWidth, 
                programmedData.atrialSensingThreshold, programmedData.atrialRefractoryPeriod)
        stateChamber2Para = self.programVentriclePara(programmedData.ventricularAmplitude, programmedData.ventricularPulseWidth,
                programmedData.ventricularSensingThreshold, programmedData.ventricularRefractoryPeriod)
        val = programmedData.getProgramModeInt()
        stateEval = (stateRateLim.value == 0 and stateChamber1Para.value == 0 and stateChamber2Para.value == 0)
        if stateEval and (val == 0 or val == 2 or val == 5 or val == 7):
            return [1, stateRateLim, stateChamber1Para]
        elif not stateEval and (val == 0 or val == 2 or val == 5 or val == 7):
            return [0, stateRateLim, stateChamber1Para]
        if stateEval and (val == 1 or val == 3 or val == 6 or val == 8):
            return [1, stateRateLim, stateChamber2Para]
        elif not stateEval and (val == 1 or val == 3 or val == 6 or val == 8):
            return [0, stateRateLim, stateChamber2Para]
        if stateEval and (val == 4 or val == 9):
            return [1, stateRateLim, stateChamber1Para, stateChamber2Para]
        elif not stateEval and (val == 4 or val == 9):
            return [0, stateRateLim, stateChamber1Para, stateChamber2Para]

    def programProgramMode(self, programMode):
        self.user.data.setProgramMode(programMode)
        return FailureCodes.VALID

    def programMisc(self, p_upperRateLim, p_lowerRateLim, p_fixedAVDelay, p_modulationSensitivity, p_rateModulation):
        """Sets current user's upper and lower rate limits, in database
        """
        if not self.validMisc(p_upperRateLim, p_lowerRateLim, p_fixedAVDelay, p_modulationSensitivity):
            return FailureCodes.INVALID_USER_INPUT
        if p_upperRateLim is not None:
            self.user.data.setUpperRateLimit(p_upperRateLim)
        if p_lowerRateLim is not None:
            self.user.data.setLowerRateLimit(p_lowerRateLim)
        if p_fixedAVDelay is not None:
            self.user.data.setFixedAVDelay(p_fixedAVDelay)
        if p_modulationSensitivity is not None:
            self.user.data.setAccelerationFactor(p_modulationSensitivity)
        self.user.data.setRateModulation(p_rateModulation)
        return FailureCodes.VALID

    def programAtriaPara(self, p_atriumAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod):
        """Sets current user's atrium data in database
        """
        if not self.validChamberPara(p_atriumAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod):
            return FailureCodes.INVALID_USER_INPUT
        if p_atriumAmp is not None:
            self.user.data.setAtrialAmplitude(p_atriumAmp)
        if p_atriumPulseWidth is not None:
            self.user.data.setAtrialPulseWidth(p_atriumPulseWidth)
        if p_atriumSensThres is not None:
            self.user.data.setAtrialSensingThreshold(p_atriumSensThres)
        if p_atriumRefracPeriod is not None:
            self.user.data.setAtrialRefractoryPeriod(p_atriumRefracPeriod)
        return FailureCodes.VALID
        
    def programVentriclePara(self, p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
        """Sets current user's ventricle data in database
        """
        if not self.validChamberPara(p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
            return FailureCodes.INVALID_USER_INPUT
        if p_ventriclePulseAmp is not None:
            self.user.data.setVentricularAmplitude(p_ventriclePulseAmp)
        if p_ventriclePulseWidth is not None:
            self.user.data.setVentricularPulseWidth(p_ventriclePulseWidth)
        if p_ventricleSensThres is not None:
            self.user.data.setVentricularSensingThreshold(p_ventricleSensThres)
        if p_ventricleRefracPeriod is not None:
            self.user.data.setVentricularRefractoryPeriod(p_ventricleRefracPeriod)
        return FailureCodes.VALID

    def getProgrammingValues(self):
        """Gets current user's programming values from database
        """
        return self.user.getProgrammingData()

    def saveProgrammingValuesToDatabase(self):
        """Saves current user's programming values to database
        """
        #print("save programming values")
        #print("username: ", self.user.username)
        #self.user.data.printData()
        self.dbManager.setUserProgramData(self.user.username, self.user.data)



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

