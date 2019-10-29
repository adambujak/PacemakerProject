# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
from DCMUserAccountManager.duam      import LoginData, UserInputProgramData
from Common.callbacks                import ApplicationCallbacks
from enum                            import Enum


class ScreenNames(Enum):
    LOGIN_SCREEN        = 0
    PROGRAMMING_SCREEN  = 1
    CREATE_USER_SCREEN  = 2

class LoginMenuData():
    def __init__(self, userNameLabel, passwordLabel, signInButtonText, newUserButtonText):
        self.fieldLabels = [userNameLabel, passwordLabel]
        self.buttonTexts = [signInButtonText, newUserButtonText]
    def setCallbacks(self, callbacks):
        self.buttonCallbacks = callbacks

class ProgramMenuData():
    def __init__(self, fieldLabels, buttonTexts, dropDownLabelText, dropDownOptions, currentOption):
        self.fieldLabels = fieldLabels
        self.buttonTexts = buttonTexts
        self.dropDownLabelText = dropDownLabelText
        self.dropDownOptions = dropDownOptions
        self.currentOption = currentOption
    def setCallbacks(self, callbacks):
        self.buttonCallbacks = callbacks

class CreateUserData():
    def __init__(self, userNameLabel, passwordLabel, createUserButtonText, cancelButtonText):
        self.fieldLabels = [userNameLabel, passwordLabel]
        self.buttonTexts = [createUserButtonText, cancelButtonText]
    def setCallbacks(self, callbacks):
        self.buttonCallbacks = callbacks


class Screen:
    def __init__(self, screenName, data):
        self.data = data
        self.screenName = screenName


loginScreen = Screen(
    ScreenNames.LOGIN_SCREEN, 
    LoginMenuData(
        C_LOGIN_USERNAME_LABEL, 
        C_LOGIN_PASSWORD_LABEL, 
        C_LOGIN_BUTTON_TEXT, 
        C_NEW_USER_BUTTON_TEXT))


programmingScreen = Screen(
    ScreenNames.PROGRAMMING_SCREEN, 
    ProgramMenuData(
        [
            [
            C_PROGRAM_UPPER_LIMIT_LABEL,
            C_PROGRAM_LOWER_LIMIT_LABEL
            ],
            [
            C_PROGRAM_ATRIUM_PULSE_AMPLITUDE,
            C_PROGRAM_ATRIUM_PULSE_WIDTH,
            C_PROGRAM_ATRIUM_SENSING_THRESHOLD,
            C_PROGRAM_ATRIUM_REFRACTORY_PERIOD
            ],
            [
            C_PROGRAM_VENTRICLE_PULSE_AMPLITUDE,
            C_PROGRAM_VENTRICLE_PULSE_WIDTH,
            C_PROGRAM_VENTRICLE_SENSING_THRESHOLD,
            C_PROGRAM_VENTRICLE_REFRACTORY_PERIOD
            ]
        ],
        [
            C_PROGRAM_BUTTON_TEXT,            
            C_PROGRAM_LOGOUT_BUTTON_TEXT  
        ],
        C_PROGRAM_DROPDOWN_LABEL,
        C_PROGRAM_DROPDOWN_OPTIONS,
        C_PROGRAM_DROPDOWN_DEFAULT))

createUserMenuScreen = Screen(
    ScreenNames.CREATE_USER_SCREEN, 
    CreateUserData(
        C_NEW_USERNAME_LABEL, 
        C_NEW_PASSWORD_LABEL, 
        C_CREATE_USER_BUTTON_TEXT,
        C_CANCEL_BUTTON_TEXT))


#############################################################
################### GUI Controller Class ####################
#############################################################

class GUIC:
    # Initialize GUI Controller #
    def __init__(self):
        self.gui = GUIAL()
        self.gui.setTitle(C_GUI_TITLE)
    
    def setCallbacks(self, callbacks):
        self.callbacks = callbacks
        loginScreen.data.setCallbacks([self.callbacks.loginButtonCB, self.callbacks.newUserButtonCB])
        programmingScreen.data.setCallbacks([self.callbacks.programButtonCB, self.callbacks.logoffButtonCB])
        createUserMenuScreen.data.setCallbacks([self.callbacks.createUserButtonCB, self.callbacks.cancelButtonCB])
    def startGUI(self):
        self.p_drawFirstScreen()

    # Draw Screen to GUI #
    def drawScreen(self, screen):
        self.gui.clearWindow()
        self.currentScreen = screen
        if (screen.screenName == ScreenNames.LOGIN_SCREEN):
            self.p_drawLoginScreen(screen.data)
        elif (screen.screenName == ScreenNames.PROGRAMMING_SCREEN):
            self.p_drawProgrammingScreen(screen.data)
        elif (screen.screenName == ScreenNames.CREATE_USER_SCREEN):
            self.p_drawCreateUserScreen(screen.data)

    # Update GUI #
    def updateGUI(self):
        self.gui.update()

    def getLoginData(self):
        """
        Retrieves data from gui input fields on Login Screen
        """
        if self.currentScreen.screenName == ScreenNames.LOGIN_SCREEN:
            entryData = self.gui.getEntryData()
            return LoginData(entryData[0], entryData[1])

    def getNewUserData(self):
        """
        Retrieves data from gui input fields on Create User Screen
        """
        if self.currentScreen.screenName == ScreenNames.CREATE_USER_SCREEN:
            entryData = self.gui.getEntryData()
            return LoginData(entryData[0], entryData[1])

    def getUserProgramData(self,):
        """
        Retrieves data from gui input fields on Programming Screen
        """
        if self.currentScreen.screenName == ScreenNames.PROGRAMMING_SCREEN:
            entryData = self.gui.getEntryData()
            for entryIndex in range(len(entryData)):
                if entryData[entryIndex] == '':
                    entryData[entryIndex] = -1;
                else:
                    entryData[entryIndex] = float(entryData[entryIndex]);
            return UserInputProgramData(entryData[0], entryData[1],entryData[2],entryData[3],entryData[4],entryData[5],entryData[6],entryData[7],entryData[8],entryData[9])

    def p_drawFirstScreen(self):
        """
        Draw first screen in application - in our case - login screen
        """
        self.drawScreen(loginScreen)

    def p_drawLoginScreen(self, data):
        """
        Draw screen of tpye login screen
        """
        self.gui.drawTwoFieldsTwoButtonLayout(
            data.fieldLabels, 
            data.buttonTexts, 
            data.buttonCallbacks)

    def p_drawProgrammingScreen(self, data):
        """
        Draw screen of type programming screen
        """
        self.gui.drawNFieldsNButtonsOneDropDownLayout(
            data.dropDownLabelText, 
            data.currentOption, 
            data.dropDownOptions, 
            data.fieldLabels,
            data.buttonTexts,
            data.buttonCallbacks)

    def p_drawCreateUserScreen(self, data): 
        """
        Draw screen of type Create User Screen
        """
        self.gui.drawTwoFieldsTwoButtonLayout(
            data.fieldLabels, 
            data.buttonTexts, 
            data.buttonCallbacks)
#ToDo: Implement
    #pass

    

    
