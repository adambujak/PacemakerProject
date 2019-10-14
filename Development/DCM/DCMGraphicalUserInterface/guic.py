# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
from Common.callbacks                import ApplicationCallbacks
from enum                            import Enum


class ScreenNames(Enum):
    LOGIN_SCREEN        = 0
    PROGRAMMING_SCREEN  = 1

class LoginMenuData():
    def __init__(self, userNameLabel, passwordLabel, signInButtonText, newUserButtonText):
        self.fieldLabels = [userNameLabel, passwordLabel]
        self.buttonTexts = [signInButtonText, newUserButtonText]



class ProgramMenuData():
    pass


class Screen:
    def __init__(self, screenName, data):
        self.data = data
        self.screenName = screenName


loginScreen = Screen(ScreenNames.LOGIN_SCREEN, LoginMenuData(C_LOGIN_USERNAME_LABEL, C_LOGIN_PASSWORD_LABEL, C_LOGIN_BUTTON_TEXT, C_LOGIN_NEW_USER_BUTTON_TEXT))
programmingScreen = Screen(ScreenNames.PROGRAMMING_SCREEN, None)


#############################################################
################### GUI Controller Class ####################
#############################################################

class GUIC:

    # Initialize GUI Controller #
    def __init__(self, callbacks):
        self.gui = GUIAL()
        self.gui.setTitle(C_GUI_TITLE)
        self.callbacks = callbacks

        self.p_drawFirstScreen()
        print("Initialized GUI Controller")
    
    # Draw Screen to GUI #
    def drawScreen(self, screen):
    
        if (screen.screenName == ScreenNames.LOGIN_SCREEN):
            self.p_drawLoginScreen(screen.data)
        elif (screen.screenName == ScreenNames.PROGRAMMING_SCREEN):
            self.p_drawProgrammingScreen(screen.data)

    # Update GUI #
    def updateGUI(self):
        self.gui.update()


    def p_drawFirstScreen(self):
        """
        Draw first screen in application - in our case - login screen
        """
        self.drawScreen(loginScreen)

    def p_drawLoginScreen(self, data):
        """
        Draw screen of tpye login screen
        """
        self.gui.drawTwoFieldsTwoButtonLayout(data.fieldLabels, data.buttonTexts, [self.callbacks.loginButtonCB, self.callbacks.newUserButtonCB])

    def p_drawProgrammingScreen(self, data):
        """
        Draw screen of tpye programming screen
        """
#ToDo: Implement
        pass
    

    
