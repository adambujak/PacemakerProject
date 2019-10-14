# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Constants Source File
# Filename: dcm_constants.py

from pathlib import Path


# GENERAL APPLICATION CONSTANTS #

C_APPLICATION_DIRECTORY        =       str(Path.cwd().resolve())                          # APPLICATION DIRECTORY 

C_ADMINISTRATOR_USERNAME       =       "Admin"
C_ADMINISTRATOR_PASSWORD       =       "42b6a520d6a1d6b695fb5ba450d065506fed2e10969287fd243efff06a6e87348ea5023c86d487f5f644404beafb9e2bc8d8587a2db10419a89b56472255335b389e79f6679a6139bcd4e39edf5d1b3029cddf8f951e29496a6cc0298df104dd"


# DATABASE CONSTANTS #

C_DATABASE_NAME                =       "dcm_database.sqlite"                              # DATABASE FILE NAME 
C_DATABASE_DIRECTORY           =       C_APPLICATION_DIRECTORY + "/src"                   # DIRECTORY OF DATABASE 
C_DATABASE_PATH                =       C_DATABASE_DIRECTORY + "/" + C_DATABASE_NAME       # DATABASE PATH
C_DATABASE_JOURNAL_MODE        =       "wal"                                              # DATABASE JOURNAL MODE
C_DATABASE_CACHE_SIZE          =       -1 * 64000                                         # DATABASE CACHE SIZE
C_DATABASE_FOREIGN_KEYS        =       1                                                  # DATABASE FOREIGN KEYS


# GUI CONSTANTS #

C_GUI_TITLE                    =       "Pacemaker DCM"                                    # TEXT TO BE SHOWN IN TITLE BAR OF GUI 

C_LOGIN_USERNAME_LABEL         =       "Username"                                         # LABEL VALUE FOR LOGIN USERNAME FIELD 
C_LOGIN_PASSWORD_LABEL         =       "Password"                                         # LABEL VALUE FOR LOGIN PASSWORD FIELD 
C_LOGIN_BUTTON_TEXT            =       "Sign In"                                          # BUTTON TEXT VALUE FOR LOGIN BUTTON
C_LOGIN_NEW_USER_BUTTON_TEXT   =       "New User"                                         # BUTTON TEXT VALUE FOR NEW USER BUTTON


C_PROGRAM_DROPDOWN_OPTIONS     =       {"AOO", "VOO", "AAO", "VVO"}                       # DROPDOWN MENU OPTIONS
C_PROGRAM_DROPDOWN_DEFAULT     =       "AOO"                                              # DEFAULT VALUE FOR DROPDOWN
C_PROGRAM_DROPDOWN_LABEL       =       "Pacing Mode"                                      # LABEL VALUE FOR DROPDOWN INDICATOR 
C_PROGRAM_UPPER_LIMIT_LABEL    =       "Upper Rate Limit"                                 # LABEL VALUE FOR UPPER RATE LIMIT FIELD 
C_PROGRAM_LOWER_LIMIT_LABEL    =       "Lower Rate Limit"                                 # LABEL VALUE FOR LOWER RATE LIMIT FIELD 
C_PROGRAM_BUTTON_TEXT          =       "Program"                                          # BUTTON TEXT VALUE FOR PROGRAM BUTTON
C_PROGRAM_LOGOUT_BUTTON_TEXT   =       "Sign Out"                                         # BUTTON TEXT VALUE FOR LOGOUT BUTTON