# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Database SQLite Manager Source File
# Filename: ddsm.py

from src.dcm_constants import *
import sqlite3

#############################################################
############### SQLite Database Manager Class ###############
#############################################################

class SDC:

    # Initialize SDC #
    def __init__(self):
        # Connect to database #
        self.database = sqlite3.connect(C_DATABASE_PATH)


    def closeDatabase(self):
        # Close database #
        self.database.close()



