# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Constants Source File
# Filename: dcm_constants.py

from pathlib import Path


# GENERAL APPLICATION CONSTANTS #

C_APPLICATION_DIRECTORY     =       str(Path.cwd().resolve())                          # APPLICATION DIRECTORY 


# DATABASE CONSTANTS #

C_DATABASE_NAME             =       "dcm_database.sqlite"                              # DATABASE FILE NAME 
C_DATABASE_DIRECTORY        =       C_APPLICATION_DIRECTORY + "/src"                   # DIRECTORY OF DATABASE 
C_DATABASE_PATH             =       C_DATABASE_DIRECTORY + "/" + C_DATABASE_NAME       # DATABASE PATH


C_INTRO_TEXT = "HEY DUDE"