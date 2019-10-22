# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Constants Source File
# Filename: dcm_constants.py

from pathlib import Path


# GENERAL APPLICATION CONSTANTS #

C_APPLICATION_DIRECTORY        =       str(Path.cwd().resolve())                          # APPLICATION DIRECTORY 

C_ADMINISTRATOR_USERNAME       =       "Admin"
C_ADMINISTRATOR_PASSWORD       =       "df2db0ece5530e6cc818cd7cce934a790210129218b6d29cde597a5716ec727f1dabf7bab86f28c641d3ec7f5202f19a380e31caffe191d29b0b4120af7b1e49fda292a4800c24a4c28c2f00e797e0cebb388d21263fb0bd39a5f4ce0f82c25d"
#Admin password is hello

# DATABASE CONSTANTS #

C_DATABASE_NAME                =       "dcm_database.sqlite"                              # DATABASE FILE NAME 
C_DATABASE_DIRECTORY           =       C_APPLICATION_DIRECTORY + "/src"                   # DIRECTORY OF DATABASE 
C_DATABASE_PATH                =       C_DATABASE_DIRECTORY + "/" + C_DATABASE_NAME       # DATABASE PATH #PacemakerProject\Development\DCM\src/src/dcm_database.sqlite
C_DATABASE_JOURNAL_MODE        =       "wal"                                              # DATABASE JOURNAL MODE
C_DATABASE_CACHE_SIZE          =       -1 * 64000                                         # DATABASE CACHE SIZE
C_DATABASE_FOREIGN_KEYS        =       1                                                  # DATABASE FOREIGN KEYS


# GUI CONSTANTS #

C_GUI_TITLE                    =       "Pacemaker DCM"                                    # TEXT TO BE SHOWN IN TITLE BAR OF GUI 

C_LOGIN_USERNAME_LABEL         =       "Username"                                         # LABEL VALUE FOR LOGIN USERNAME FIELD 
C_LOGIN_PASSWORD_LABEL         =       "Password"                                         # LABEL VALUE FOR LOGIN PASSWORD FIELD 
C_LOGIN_BUTTON_TEXT            =       "Login"                                          # BUTTON TEXT VALUE FOR LOGIN BUTTON
C_NEW_USER_BUTTON_TEXT   	   =       "New User?"                                         # BUTTON TEXT VALUE FOR NEW USER BUTTON


C_PROGRAM_DROPDOWN_OPTIONS     =       {"AOO", "VOO", "AAO", "VVO"}                       # DROPDOWN MENU OPTIONS
C_PROGRAM_DROPDOWN_DEFAULT     =       "AOO"                                              # DEFAULT VALUE FOR DROPDOWN
C_PROGRAM_DROPDOWN_LABEL       =       "Pacing Mode"                                      # LABEL VALUE FOR DROPDOWN INDICATOR 
C_PROGRAM_UPPER_LIMIT_LABEL    =       "Upper Rate Limit"                                 # LABEL VALUE FOR UPPER RATE LIMIT FIELD 
C_PROGRAM_LOWER_LIMIT_LABEL    =       "Lower Rate Limit"                                 # LABEL VALUE FOR LOWER RATE LIMIT FIELD 
C_PROGRAM_BUTTON_TEXT          =       "Program"                                          # BUTTON TEXT VALUE FOR PROGRAM BUTTON
C_PROGRAM_LOGOUT_BUTTON_TEXT   =       "Sign Out"                                         # BUTTON TEXT VALUE FOR LOGOUT BUTTON

C_CREATE_USER_BUTTON_TEXT	   = 	   "Create New User"
C_CANCEL_BUTTON_TEXT		   = 	   "Cancel"