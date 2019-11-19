# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database Controller Source File
# Filename: dbc.py

from src.dcm_constants import *
from DCMDatabase.dbpm  import *

#############################################################
################ Database Controller Class ##################
#############################################################

class DBC:

    # Initialize DBC #
    def __init__(self):
        # Start Database Manager #
        self.dbManager = DBPM() 


    def closeDatabase(self):
        # Close database #
        self.dbManager.closeDatabase()

    # def 

