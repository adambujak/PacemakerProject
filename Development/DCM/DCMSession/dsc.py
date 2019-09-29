# Author: Adam Bujak
# Date Created: Saturday, September 28, 2019
# Description: DCM Session Controller Source File
# Filename: dsc.py

from src.dcm_constants import *
from DCMDatabase.dbpm  import *
from enum              import Enum

import hashlib, binascii, os


#############################################################
####################### Sessions Enum #######################
#############################################################

class SessionStates(Enum):
    LOGGED_OUT    = 0
    LOGGED_IN     = 1

# class User:

#     def __init__(self):



#############################################################
################# Session Controller Class ##################
#############################################################

class DSC:

    # Initialize DSC #
    def __init__(self):
        # Start Database Manager #
        self.dbManager = DBPM()
        self.user      = None
        self.state     = SessionStates.LOGGED_OUT
        self.dbManager.createUser("Ada", "pasdscsword", "doctor")
        self.dbManager.searchForUser("Ada")



    # def signInUser(self, username, password, adminPassword):
    #     # Handle signing in

    #     # Check user to make sure it exists
    #     if (self.dbManager.userExists):
    #         # Check password
    #         # Set permissions
    #         # return true
    #     else
    #         return False



 
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

