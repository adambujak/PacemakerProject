# Author: Adam Bujak
# Date Created: Saturday, September 28, 2019
# Description: DCM User Account Manager Source File
# Filename: duam.py

from src.dcm_constants import *
from DCMDatabase.dbpm  import *
from enum              import Enum

import hashlib, binascii, os


#############################################################
####################### Sessions Enum #######################
#############################################################


class FailureCodes(Enum):
    SUCCESS             = 0
    INCORRECT_PASSWORD  = 1
    INCORRECT_USERNAME  = 2
    EXISTING_USER       = 3
    INVALID_CREDENTIALS = 4
    MISSING_PERMISSIONS = 5
    TOO_MANY_USERS      = 6

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

class ProgrammedData:
    def __init__(self, p_upperRateLim, p_lowerRateLim, p_atriumPulseAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod,  p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
        self.upperRateLim = p_upperRateLim
        self.lowerRateLim = p_lowerRateLim
        self.atriumPulseAmp = p_atriumPulseAmp
        self.atriumPulseWidth = p_atriumPulseWidth
        self.atriumSensThres = p_atriumSensThres
        self.atriumRefracPeriod = p_atriumRefracPeriod
        self.ventriclePulseAmp = p_ventriclePulseAmp
        self.ventriclePulseWidth = p_ventriclePulseWidth
        self.ventricleSensThres = p_ventricleSensThres
        self.ventricleRefracPeriod = p_ventricleRefracPeriod


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
        self.dbManager.createUser(C_ADMINISTRATOR_USERNAME, C_ADMINISTRATOR_PASSWORD, UserRole.ADMIN)

    def makeNewUser(self,p_loginData, p_adminPassword):
        """Adds new user to database.
        p_password must not be hashed,
        returns FailureCode
        """
        p_username = p_loginData.username
        p_password = hash_password(p_loginData.password)
        p_adminPassword = hash_password(p_adminPassword)
        if self.validUser():
            return FailureCodes.MISSING_PERMISSIONS
        if not self.validNumUsers():
            return FailureCodes.TOO_MANY_USERS
 
#ToDo: add max 10 user limit constraint

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
        self.dbManager.createUser(p_username, p_password, UserRole.USER)
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

    def validNumUsers(self):
        if self.dbManager.getNumUsers() >= 10:
            return False
        return True

    def programRateLim(self,p_upperRateLim, p_lowerRateLim):
        """Sets device's rates upper & lower limits
        """
        pass

    def programAtriaPara(self,p_atriumPulseAmp, p_atriumPulseWidth, p_atriumSensThres, p_atriumRefracPeriod):
        """Sets device's programmable parameters for the atria
        """
        pass

    def programVentriclePara(self,p_ventriclePulseAmp, p_ventriclePulseWidth, p_ventricleSensThres, p_ventricleRefracPeriod):
        """Sets device's programmable parameters for the ventricles
        """
        pass

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

