# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
from enum                            import Enum



class ScreenNames(Enum):
    LOGIN_SCREEN        = 0
    PROGRAMMING_SCREEN  = 1

class LoginMenuData():
    pass

class LoginMenuData():
    pass


class Screen:
    def __init__(self, screenName, data):
        self.data = data
        self.screenName = screenName


loginScreen = Screen(ScreenNames.LOGIN_SCREEN, 1)
programmingScreen = Screen(ScreenNames.PROGRAMMING_SCREEN, 1)



def signInCallback():
    print("button clickled")
#############################################################
################### GUI Controller Class ####################
#############################################################

class GUIC:

    # Initialize GUI Controller #
    def __init__(self):
        self.gui = GUIAL()
        self.gui.setTitle(C_GUI_TITLE)
        self.p_drawFirstScreen()
        print("Initialized GUI Controller")
    
    # Draw Screen to GUI #
    def drawScreen(self, screen):
# ToDo: implement screen object 
    
        if (screen.screenName == ScreenNames.LOGIN_SCREEN):
            self.p_drawLoginScreen()
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

    def p_drawLoginScreen(self):
        """
        Draw screen of tpye login screen
        """
        self.gui.drawTwoFieldsOneButtonLayout(C_LOGIN_USERNAME_LABEL, 
            C_LOGIN_PASSWORD_LABEL,
            C_LOGIN_BUTTON_TEXT,
            None)
# ToDo: change callback
    def p_drawProgrammingScreen(self, data):
        """
        Draw screen of tpye programming screen
        """
        pass
    

    
