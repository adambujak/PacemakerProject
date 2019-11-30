# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Constants Source File
# Filename: dcm_constants.py

from pathlib import Path


# GENERAL APPLICATION CONSTANTS #

C_APPLICATION_DIRECTORY                    =        str(Path.cwd().resolve())                          # APPLICATION DIRECTORY 

C_ADMINISTRATOR_USERNAME                   =       "Admin"
C_ADMINISTRATOR_PASSWORD                   =       "0b4548dfadaf4ad5c8c9ab4bf1fc95247ebf358c1952e026f67fccc7a7c08203577c3c316bfda6a290e6b68feece3f86ec5696a74389fb04b45190af212c79233864d6fddb42626947b5412d337d337f4471ca1e1bc9b89306784927048141a4"
#Admin password is 'C_ADMIN_PASSWORD'

# DATABASE CONSTANTS #

C_DATABASE_NAME                            =       "dcm_database.sqlite"                              # DATABASE FILE NAME 
C_DATABASE_DIRECTORY                       =        C_APPLICATION_DIRECTORY + "/src"                   # DIRECTORY OF DATABASE 
C_DATABASE_PATH                            =        C_DATABASE_DIRECTORY + "/" + C_DATABASE_NAME       # DATABASE PATH #PacemakerProject\Development\DCM\src/src/dcm_database.sqlite
C_DATABASE_JOURNAL_MODE                    =       "wal"                                              # DATABASE JOURNAL MODE
C_DATABASE_CACHE_SIZE                      =       -1 * 64000                                         # DATABASE CACHE SIZE
C_DATABASE_FOREIGN_KEYS                    =        1                                                  # DATABASE FOREIGN KEYS


# GUI CONSTANTS #

C_GUI_TITLE                                =       "Pacemaker DCM"                                    # TEXT TO BE SHOWN IN TITLE BAR OF GUI 

C_LOGIN_USERNAME_LABEL                     =       "Username"                                         # LABEL VALUE FOR LOGIN USERNAME FIELD 
C_LOGIN_PASSWORD_LABEL                     =       "Password"                                         # LABEL VALUE FOR LOGIN PASSWORD FIELD 
C_LOGIN_BUTTON_TEXT                        =       "Login"                                            # BUTTON TEXT VALUE FOR LOGIN BUTTON
C_NEW_USER_BUTTON_TEXT                     =       "New User?"                                        # BUTTON TEXT VALUE FOR NEW USER BUTTON
C_NEW_USERNAME_LABEL                       =       "Username\n min length: 4 char"                    # LABEL VALUE FOR NEW USERNAME FIELD 
C_NEW_PASSWORD_LABEL                       =       "Password\n min length: 4 char"                    # LABEL VALUE FOR NEW PASSWORD FIELD 


C_PROGRAM_UPPER_LIMIT_LABEL                =       "Upper Rate Limit\n (BPM)"                         # LABEL VALUE FOR UPPER RATE LIMIT FIELD
C_PROGRAM_LOWER_LIMIT_LABEL                =       "Lower Rate Limit\n (BPM)"                         # LABEL VALUE FOR LOWER RATE LIMIT FIELD
C_PROGRAM_ATRIUM_PULSE_AMPLITUDE           =       "Atrium Pulse Amplitude\n (mV)"                    # LABEL VALUE FOR ATRIUM PULSE AMPLITUDE
C_PROGRAM_ATRIUM_PULSE_WIDTH               =       "Atrium Pulse Width\n (ms)"                        # LABEL VALUE FOR ATRIUM PULSE WIDTH
C_PROGRAM_ATRIUM_SENSING_THRESHOLD         =       "Atrium Sensing Threshold\n (mV)"                  # LABEL VALUE FOR ATRIUM SENSING THRESHOLD
C_PROGRAM_ATRIUM_REFRACTORY_PERIOD         =       "Atrium Refractory period\n (ms)"                  # LABEL VALUE FOR ATRIUM REFRACTORY PERIOD
C_PROGRAM_VENTRICLE_PULSE_AMPLITUDE        =       "Ventricle Pulse Amplitude\n (mV)"              # LABEL VALUE FOR VENTRICLE PULSE AMPLITUDE
C_PROGRAM_VENTRICLE_PULSE_WIDTH            =       "Ventricle Pulse Width\n (ms)"                     # LABEL VALUE FOR VENTRICLE PULSE WIDTH
C_PROGRAM_VENTRICLE_SENSING_THRESHOLD      =       "Ventricle Sensing Threshold\n (mV)"               # LABEL VALUE FOR VENTRICLE SENSING THRESHOLD
C_PROGRAM_VENTRICLE_REFRACTORY_PERIOD      =       "Ventricle Refractory period\n (ms)"               # LABEL VALUE FOR VENTRICLE REFRACTORY PERIOD
C_PROGRAM_DROPDOWN_OPTIONS                 =      ["AOO", "AAI", "VOO", "VVI"]                        # DROPDOWN MENU OPTIONS
C_PROGRAM_DROPDOWN_DEFAULT                 =       "AOO"                                              # DEFAULT VALUE FOR DROPDOWN
C_PROGRAM_DROPDOWN_LABEL                   =       "Pacing Mode"                                      # LABEL VALUE FOR DROPDOWN INDICATOR 
C_PROGRAM_BUTTON_TEXT                      =       "Program"                                          # BUTTON TEXT VALUE FOR PROGRAM BUTTON
C_PROGRAM_LOGOUT_BUTTON_TEXT               =       "Sign Out"                                         # BUTTON TEXT VALUE FOR LOGOUT BUTTON

C_CREATE_USER_BUTTON_TEXT                  =       "Create New User"
C_CANCEL_BUTTON_TEXT                       =       "Cancel"


# PROGRAM DATA DEFAULTS #

C_DEFAULT_PROGRAM_MODE                     =       "AOO"
C_DEFAULT_LOWER_RATE_LIMIT                 =        60          # BPM
C_DEFAULT_UPPER_RATE_LIMIT                 =        120         # BPM
C_DEFAULT_ATRIAL_AMPLITUDE                 =        3500        # mV
C_DEFAULT_ATRIAL_PULSE_WIDTH               =        10          # ms
C_DEFAULT_ATRIAL_SENSING_THRESHOLD         =        2640        # mV
C_DEFAULT_ATRIAL_REFRACTORY_PERIOD         =        250         # ms
C_DEFAULT_VENTRICULAR_AMPLITUDE            =        3500        # mV
C_DEFAULT_VENTRICULAR_PULSE_WIDTH          =        10          # ms
C_DEFAULT_VENTRICULAR_SENSING_THRESHOLD    =        2640        # mV
C_DEFAULT_VENTRICULAR_REFRACTORY_PERIOD    =        320         # ms
C_DEFAULT_FIXED_AV_DELAY                   =        150         # ms
C_DEFAULT_RATE_MODULATION                  =        0           # bool, off or on
C_DEFAULT_MODULATION_SENSITIVITY           =        8           # int, 1 - 16



# SERIAL COM DEFAULTS #

C_SERIAL_COM_PORT                          =       "COM10"
C_SERIAL_BAUD_RATE                         =        9600
C_SERIAL_TIMEOUT                           =        1

C_SERIAL_START_BYTE                        =        0x16

C_SERIAL_PARAMETER_START_BYTE              =        0x55
C_SERIAL_PARAMETER_BYTE_CNT                =        21

C_SERIAL_EGRAM_START_BYTE                  =        0x47
C_SERIAL_EGRAM_STOP_BYTE                   =        0x62

C_SERIAL_ECHO_COMMAND_BYTE                 =        0x22

C_SERIAL_ACK_RECEIVE_STRING                =       "ACK"

C_SERIAL_ACK_RECEIVE_TIMEOUT               =        5

C_SERIAL_PARAMETER_PROGRAM_PACK            =       "<5B2H2B5H2B"
C_SERIAL_PARAMETER_ECHO_PACK               =       "<2B21x"
C_SERIAL_PARAMETER_ECHO_UNPACK             =       "<3B2H2B5H2B"

C_SERIAL_EGRAM_ECHO_PACK                   =       "<2B21x"
C_SERIAL_EGRAM_ECHO_UNPACK                 =       "<2d5x"

