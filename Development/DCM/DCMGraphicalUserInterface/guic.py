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
    def __init__(self, userNameLabel, passwordLabel, buttonText):
        self.userNameLabel = userNameLabel
        self.passwordLabel = passwordLabel
        self.buttonText    = buttonText


class ProgramMenuData():
    pass


class Screen:
    def __init__(self, screenName, data):
        self.data = data
        self.screenName = screenName


loginScreen = Screen(ScreenNames.LOGIN_SCREEN, LoginMenuData(C_LOGIN_USERNAME_LABEL, C_LOGIN_PASSWORD_LABEL, C_LOGIN_BUTTON_TEXT))
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
# ToDo: implement screen object 
    
        if (screen.screenName == ScreenNames.LOGIN_SCREEN):
            self.p_drawLoginScreen(screen.data)
        elif (screen.screenName == ScreenNames.PROGRAMMING_SCREEN):
            pass

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
        self.gui.drawTwoFieldsOneButtonLayout(data.userNameLabel, data.passwordLabel, data.buttonText, self.callbacks.loginButtonCB)

    def p_drawProgrammingScreen(self, data):
        """
        Draw screen of tpye programming screen
        """
#ToDo: Implement
        pass
    

    
