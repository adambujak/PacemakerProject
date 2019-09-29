# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database Peewee Manager Source File
# Filename: dbpm.py

from src.dcm_constants import *
from peewee            import *


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

    def createUser(self, i_username, i_password, i_role):
        # Create new user
        self.User.create(username = i_username, password = i_password, role = i_role)

    def searchForUser(self, username):
        query = self.User.select().order_by(self.User.username)
        query = query.where(self.User.username.contains(username))
        for user in query:
            username = user.username
            print(username)


    # Private Methods #
    def p_createDataTables(self):
        # Create all tables used in application 
        self.User.create_table()



    ################ Peweee Database Definitions ################

    # model definition -- the standard "pattern" is to define a base model class
    # that specifies which database to use.  then, any subclasses will automatically
    # use the correct storage.
    class BaseModel(Model):
        class Meta:
            database = database

    class User(BaseModel):
        username = CharField(unique=True)  # User's username
        password = CharField()             # Hashed value of user's password
        role     = CharField()             # User's role, ie. doctor, nurse, admin, etc.


