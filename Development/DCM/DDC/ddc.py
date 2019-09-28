# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database Controller Source File
# Filename: ddc.py

# from src.dcm_constants import *
# from DCM.sdc import *

# #############################################################
# ################ Database Controller Class ##################
# #############################################################

# class DDC:

#     # Initialize SDC #
#     def __init__(self):
#         # Connect to database #
#         self.database = sqlite3.connect(C_DATABASE_PATH)


#     def closeDatabase(self):
#         # Close database #
#         self.database.close()

#     def 


from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.