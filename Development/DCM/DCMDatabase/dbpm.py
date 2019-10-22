# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database Peewee Manager Source File
# Filename: dbpm.py

from src.dcm_constants           import *
from peewee                      import *
import DCMUserAccountManager.duam  


database = SqliteDatabase(C_DATABASE_PATH, pragmas={
    'journal_mode': C_DATABASE_JOURNAL_MODE,
    'cache_size': C_DATABASE_CACHE_SIZE,
    'foreign_keys': C_DATABASE_FOREIGN_KEYS})


#############################################################
############### Peweee Database Manager Class ###############
#############################################################

class DBPM:

    # Public Methods #
    def __init__(self):
        # Connect to database #
        self.database = database
        self.p_createDataTables()

    def closeDatabase(self):
        # Close database #
        return self.database.close()

    def getDatabaseInstance(self):
        # Return database instance
        return self.database()

    def createUser(self, p_username, p_password, p_role):
        # Create new user
        self.User1.create(username = p_username, password = p_password, role = p_role)

    def userExists(self, p_username):
        """Checks if user exits, 
        true = exists,
        false = does not exist
        """
        query = self.User1.select().where(self.User1.username.contains(p_username))
        # Loop through users in query
        for user in query:
            # If found exact match, return true
            if user.username == p_username:
                return True
        # Return false if exact match not found
        return False

    def getUserData(self, p_username):
        query = self.User1.select().where(self.User1.username.contains(p_username))
        # Loop through users in query
        for user in query:
            # If found exact match, return true
            if user.username == p_username:
                #print(user.password + user.password + user.role)

                return DCMUserAccountManager.duam.User(user.password, user.password, user.role)
        # Return None if exact match not found
        return None

    def changeUserPassword(self, p_username, p_password):
        # query = self.User1.select().where(self.User1.username.contains(p_username))
        # # Loop through users in query
        # for user in query:
        #     # If found exact match, return true
        #     if user.username == p_username:
        #         return User(user.password, user.password, user.role)
        # # Return None if exact match not found
        # return None
#ToDo: Implement
        pass

    # Private Methods #
    def p_createDataTables(self):
        # Create all tables used in application 
        self.User1.create_table()

    ################ Peweee Database Definitions ################

    # model definition -- the standard "pattern" is to define a base model class
    # that specifies which database to use.  then, any subclasses will automatically
    # use the correct storage.
    class BaseModel(Model):
        class Meta:
            database = database

    class User1(BaseModel):
        username = CharField(unique=True)  # User's username
        password = CharField()             # Hashed value of user's password
        role     = CharField()             # User's role, ie. doctor, nurse, admin, etc.



