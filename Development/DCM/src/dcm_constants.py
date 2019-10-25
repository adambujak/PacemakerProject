# Author: Adam Bujak
# Date Created: Friday, September 27, 2019
# Description: DCM Constants Source File
# Filename: dcm_constants.py

from pathlib import Path


# GENERAL APPLICATION CONSTANTS #

C_APPLICATION_DIRECTORY        		  =       str(Path.cwd().resolve())                          # APPLICATION DIRECTORY 

C_ADMINISTRATOR_USERNAME       		  =       "Admin"
C_ADMINISTRATOR_PASSWORD       		  =       "0b4548dfadaf4ad5c8c9ab4bf1fc95247ebf358c1952e026f67fccc7a7c08203577c3c316bfda6a290e6b68feece3f86ec5696a74389fb04b45190af212c79233864d6fddb42626947b5412d337d337f4471ca1e1bc9b89306784927048141a4"
#Admin password is 'C_ADMIN_PASSWORD'

# DATABASE CONSTANTS #

C_DATABASE_NAME                		  =       "dcm_database.sqlite"                              # DATABASE FILE NAME 
C_DATABASE_DIRECTORY           		  =       C_APPLICATION_DIRECTORY + "/src"                   # DIRECTORY OF DATABASE 
C_DATABASE_PATH               	 	  =       C_DATABASE_DIRECTORY + "/" + C_DATABASE_NAME       # DATABASE PATH #PacemakerProject\Development\DCM\src/src/dcm_database.sqlite
C_DATABASE_JOURNAL_MODE        		  =       "wal"                                              # DATABASE JOURNAL MODE
C_DATABASE_CACHE_SIZE          		  =       -1 * 64000                                         # DATABASE CACHE SIZE
C_DATABASE_FOREIGN_KEYS        		  =       1                                                  # DATABASE FOREIGN KEYS


# GUI CONSTANTS #

C_GUI_TITLE               	     	  =       "Pacemaker DCM"                                    # TEXT TO BE SHOWN IN TITLE BAR OF GUI 

C_LOGIN_USERNAME_LABEL     	    	  =       "Username"                                         # LABEL VALUE FOR LOGIN USERNAME FIELD 
C_LOGIN_PASSWORD_LABEL    		 	  =       "Password"                                         # LABEL VALUE FOR LOGIN PASSWORD FIELD 
C_LOGIN_BUTTON_TEXT           		  =       "Login"                                            # BUTTON TEXT VALUE FOR LOGIN BUTTON
C_NEW_USER_BUTTON_TEXT   	   		  =       "New User?"                                        # BUTTON TEXT VALUE FOR NEW USER BUTTON


C_PROGRAM_UPPER_LIMIT_LABEL    		  =       "Upper Rate Limit"                                 # LABEL VALUE FOR UPPER RATE LIMIT FIELD 
C_PROGRAM_LOWER_LIMIT_LABEL    		  =       "Lower Rate Limit"                                 # LABEL VALUE FOR LOWER RATE LIMIT FIELD 
C_PROGRAM_ATRIUM_PULSE_AMPLITUDE 	  =		  "Atrium Pulse Amplitude"						     # LABEL VALUE FOR ATRIUM PULSE AMPLITUDE
C_PROGRAM_ATRIUM_PULSE_WIDTH	 	  =		  "Atrium Pulse Width"						   	     # LABEL VALUE FOR ATRIUM PULSE WIDTH
C_PROGRAM_ATRIUM_SENSING_THRESHOLD	  =		  "Atrium Sensing Threshold"						 # LABEL VALUE FOR ATRIUM SENSING THRESHOLD
C_PROGRAM_ATRIUM_REFRACTORY_PERIOD 	  =		  "Atrium Refractory period"						 # LABEL VALUE FOR ATRIUM REFRACTORY PERIOD
C_PROGRAM_VENTRICLE_PULSE_AMPLITUDE   =		  "Ventricle Pulse Amplitude"						 # LABEL VALUE FOR VENTRICLE PULSE AMPLITUDE
C_PROGRAM_VENTRICLE_PULSE_WIDTH	 	  =		  "Ventricle Pulse Width"						   	 # LABEL VALUE FOR VENTRICLE PULSE WIDTH
C_PROGRAM_VENTRICLE_SENSING_THRESHOLD =		  "Ventricle Sensing Threshold"						 # LABEL VALUE FOR VENTRICLE SENSING THRESHOLD
C_PROGRAM_VENTRICLE_REFRACTORY_PERIOD =		  "Ventricle Refractory period"						 # LABEL VALUE FOR VENTRICLE REFRACTORY PERIOD
C_PROGRAM_DROPDOWN_OPTIONS     		  =       {"AOO", "AAI", "VOO", "VVI"}                       # DROPDOWN MENU OPTIONS
C_PROGRAM_DROPDOWN_DEFAULT     		  =       "AOO"                                              # DEFAULT VALUE FOR DROPDOWN
C_PROGRAM_DROPDOWN_LABEL       		  =       "Pacing Mode"                                      # LABEL VALUE FOR DROPDOWN INDICATOR 
C_PROGRAM_BUTTON_TEXT          		  =       "Program"                                          # BUTTON TEXT VALUE FOR PROGRAM BUTTON
C_PROGRAM_LOGOUT_BUTTON_TEXT   		  =       "Sign Out"                                         # BUTTON TEXT VALUE FOR LOGOUT BUTTON

C_CREATE_USER_BUTTON_TEXT	   		  = 	  "Create New User"
C_CANCEL_BUTTON_TEXT		   		  = 	  "Cancel"