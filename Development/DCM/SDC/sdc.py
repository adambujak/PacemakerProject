# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: SQLite Database Controller Source File
# Filename: sdc.py

from src.dcm_constants import *
import sqlite3

#############################################################
############# SQLite Database Controller Class ##############
#############################################################

class SDC:

    # Initialize SDC #
    def __init__(self):
        # Connect to database #
        print(C_DATABASE_PATH)
        database = sqlite3.connect(C_DATABASE_PATH)
        database.close()


