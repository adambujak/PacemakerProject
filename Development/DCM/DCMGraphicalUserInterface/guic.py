# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
from DCMUserAccountManager.duam      import LoginData
from Common.callbacks                import ApplicationCallbacks
from enum                            import Enum


class ScreenNames(Enum):
    LOGIN_SCREEN        = 0
    PROGRAMMING_SCREEN  = 1

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
        C_LOGIN_NEW_USER_BUTTON_TEXT))


programmingScreen = Screen(
    ScreenNames.PROGRAMMING_SCREEN, 
    ProgramMenuData(
        [
            C_PROGRAM_UPPER_LIMIT_LABEL, 
            C_PROGRAM_LOWER_LIMIT_LABEL
        ],
        [
            C_PROGRAM_BUTTON_TEXT,            
            C_PROGRAM_LOGOUT_BUTTON_TEXT  
        ],
        C_PROGRAM_DROPDOWN_LABEL,
        C_PROGRAM_DROPDOWN_OPTIONS,
        C_PROGRAM_DROPDOWN_DEFAULT))


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

    # Update GUI #
    def updateGUI(self):
        self.gui.update()

    def getLoginData(self):
        if self.currentScreen.screenName == ScreenNames.LOGIN_SCREEN:
            entryData = self.gui.getEntryData()
            return LoginData(entryData[0], entryData[1])


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
        Draw screen of tpye programming screen
        """
        self.gui.drawNFieldsNButtonsOneDropDownLayout(
            data.dropDownLabelText, 
            data.currentOption, 
            data.dropDownOptions, 
            data.fieldLabels,
            data.buttonTexts,
            data.buttonCallbacks)
#ToDo: Implement
        pass
    

    
