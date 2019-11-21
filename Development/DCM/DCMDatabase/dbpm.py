# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database Peewee Manager Source File
# Filename: dbpm.py

from src.dcm_constants           import *
from peewee                      import *
from Common.datatypes            import PacemakerParameterData


database = SqliteDatabase(C_DATABASE_PATH, pragmas={
    'journal_mode': C_DATABASE_JOURNAL_MODE,
    'cache_size'  : C_DATABASE_CACHE_SIZE,
    'foreign_keys': C_DATABASE_FOREIGN_KEYS})


class User:
    def __init__(self, p_username, p_password, p_userRole, p_data):
        self.username    = p_username
        self.password    = p_password
        self.role        = p_userRole
        self.data        = p_data

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getRole(self):
        return self.role
    def getProgrammingData(self):
        return self.data




#############################################################
############### Database Peewee Manager Class ###############
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

    def createUser(self, p_username, p_password, p_role, p_data):
        # Create new user
        # Create data variable

        data = DatabaseProgramData.create( 
            programMode                 = p_data.programMode,
            upperRateLimit              = p_data.upperRateLimit,
            lowerRateLimit              = p_data.lowerRateLimit,
            atrialAmplitude             = p_data.atrialAmplitude,
            atrialPulseWidth            = p_data.atrialPulseWidth,
            atrialSensingThreshold      = p_data.atrialSensingThreshold,
            atrialRefractoryPeriod      = p_data.atrialRefractoryPeriod,
            ventricularAmplitude        = p_data.ventricularAmplitude,
            ventricularPulseWidth       = p_data.ventricularPulseWidth,
            ventricularSensingThreshold = p_data.ventricularSensingThreshold,
            ventricularRefractoryPeriod = p_data.ventricularRefractoryPeriod,
            fixedAVDelay                = p_data.fixedAVDelay, 
            accelerationFactor          = p_data.accelerationFactor,
            rateModulation              = p_data.rateModulation)

        DatabaseUserData.create(username = p_username, password = p_password, role = p_role, data = data)


    def userExists(self, p_username):
        """Checks if user exits, 
        true = exists,
        false = does not exist
        """
        query = DatabaseUserData.select().where(DatabaseUserData.username.contains(p_username))
        # Loop through users in query
        for user in query:
            # If found exact match, return true
            if user.username == p_username:
                return True
        # Return false if exact match not found
        return False

    def getUserData(self, p_username):
        query = DatabaseUserData.select().where(DatabaseUserData.username.contains(p_username))
        # Loop through users in query
        for user in query:
            # If found exact match, return true
            if user.username == p_username:
                data = PacemakerParameterData(
                    user.data.programMode,
                    user.data.upperRateLimit,
                    user.data.lowerRateLimit,
                    user.data.atrialAmplitude,
                    user.data.atrialPulseWidth,
                    user.data.atrialSensingThreshold,
                    user.data.atrialRefractoryPeriod,
                    user.data.ventricularAmplitude,
                    user.data.ventricularPulseWidth,
                    user.data.ventricularSensingThreshold,
                    user.data.ventricularRefractoryPeriod,
                    user.data.fixedAVDelay,
                    user.data.accelerationFactor,
                    user.data.rateModulation)    
                
                return User(user.username, user.password, user.role, data) #look to resolve by implementing signout, log in iff logged out***
        # Return None if exact match not found
        return None


    def setUserProgramData(self, p_username, p_data):
        """ Updates user program data
        """
        data = DatabaseProgramData.create( 
            programMode                 = p_data.programMode,
            lowerRateLimit              = p_data.lowerRateLimit,
            upperRateLimit              = p_data.upperRateLimit,
            atrialAmplitude             = p_data.atrialAmplitude,
            atrialPulseWidth            = p_data.atrialPulseWidth,
            atrialSensingThreshold      = p_data.atrialSensingThreshold,
            atrialRefractoryPeriod      = p_data.atrialRefractoryPeriod,
            ventricularAmplitude        = p_data.ventricularAmplitude,
            ventricularPulseWidth       = p_data.ventricularPulseWidth,
            ventricularSensingThreshold = p_data.ventricularSensingThreshold,
            ventricularRefractoryPeriod = p_data.ventricularRefractoryPeriod,
            fixedAVDelay                = p_data.fixedAVDelay, 
            accelerationFactor          = p_data.accelerationFactor,
            rateModulation              = p_data.rateModulation)

        res = (DatabaseUserData
            .update({DatabaseUserData.data: data})
            .where(DatabaseUserData.username == p_username)
            .execute())

    def getNumUsers(self):
        query = DatabaseUserData.select()
        return len(query)

    def changeUserPassword(self, p_username, p_password):
        # query = DatabaseUserData.select().where(DatabaseUserData.username.contains(p_username))
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
        DatabaseUserData.create_table()
        DatabaseProgramData.create_table()



################ Peweee Database Definitions ################

# model definition -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = database

class DatabaseProgramData(BaseModel):
    programMode                 = CharField()
    lowerRateLimit              = IntegerField()            
    upperRateLimit              = IntegerField()    
    atrialAmplitude             = FloatField() 
    atrialPulseWidth            = FloatField()    
    atrialSensingThreshold      = FloatField()  
    atrialRefractoryPeriod      = IntegerField()    
    ventricularAmplitude        = FloatField()      
    ventricularPulseWidth       = FloatField()   
    ventricularSensingThreshold = FloatField()
    ventricularRefractoryPeriod = IntegerField()
    fixedAVDelay                = IntegerField()
    accelerationFactor          = IntegerField()
    rateModulation              = BooleanField()

          


class DatabaseUserData(BaseModel):
    username = CharField(unique=True)                                 # User's username
    password = CharField()                                            # Hashed value of user's password
    role     = CharField()                                            # User's role, ie. doctor, nurse, admin, etc.
    data     = ForeignKeyField(DatabaseProgramData)                   # User data