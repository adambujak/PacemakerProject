# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
from src.dcm_constants               import *
from DCMUserAccountManager.duam      import LoginData
from Common.datatypes                import PacemakerParameterData
from Common.callbacks                import ApplicationCallbacks
from Common.failCodes                import FailureCodes
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
    def setProgrammingValues(self, data):
        self.programmingValues = data
    def getProgrammingValues(self):
        return self.programmingValues


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


# added mode property to program screen

programmingScreen = Screen(
    ScreenNames.PROGRAMMING_SCREEN, 
    ProgramMenuData(
        [
            [
            C_PROGRAM_UPPER_LIMIT_LABEL,
            C_PROGRAM_LOWER_LIMIT_LABEL,
            C_PROGRAM_MODULATION_SENSITIVITY_LABEL,
            C_PROGRAM_FIXED_AV_DELAY_LABEL
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
            C_PROGRAM_ECHO_BUTTON_TEXT,            
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
        programmingScreen.data.setCallbacks([self.callbacks.programButtonCB, self.callbacks.echoButtonCB, self.callbacks.logoffButtonCB])
        createUserMenuScreen.data.setCallbacks([self.callbacks.createUserButtonCB, self.callbacks.cancelButtonCB])
    
    def setProgrammingValues(self, data):
        """ Sets the programming values in our program menu data
            @param data - type: PacemakerParameterData
        """
        programmingScreen.data.setProgrammingValues(data)

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

    def getPacemakerParameterData(self):
        """
        Retrieves data from gui input fields on Programming Screen
        """
        #use PacemakerParameterData class to pass data to main
        if self.currentScreen.screenName == ScreenNames.PROGRAMMING_SCREEN:
            programMode = self.gui.getProgramMode()
            entryData = self.gui.getEntryData()
            for entryIndex in range(len(entryData)):
                if entryData[entryIndex] == '':
                    entryData[entryIndex] = None
                elif entryData[entryIndex].isdigit():
                    entryData[entryIndex] = int(entryData[entryIndex])
                else:
                    entryData[entryIndex] = -1
            if programMode == "AOO" or programMode == "AAI":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], entryData[2], entryData[3], entryData[4], entryData[5], None, None, None, None, None, None, 0)
            if programMode == "VOO" or programMode == "VVI":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], None, None, None, None, entryData[2], entryData[3], entryData[4], entryData[5], None, None, 0)
            if programMode == "AOOR" or programMode == "AAIR":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], entryData[3], entryData[4], entryData[5], entryData[6], None, None, None, None, None, entryData[2], 1)
            if programMode == "VOOR" or programMode == "VVIR":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], None, None, None, None, entryData[3], entryData[4], entryData[5], entryData[6], None, entryData[2], 1)
            if programMode == "DOO":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], entryData[3], entryData[4], entryData[5], entryData[6], entryData[7], entryData[8], entryData[9], entryData[10], entryData[2], None, 0)
            if programMode == "DOOR":
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], entryData[4], entryData[5], entryData[6], entryData[7], entryData[8], entryData[9], entryData[10], entryData[11], entryData[3], entryData[2], 1)
            
    def drawErrorMessage(self, errorCodes, thisScreen):
        if (thisScreen == ScreenNames.LOGIN_SCREEN.value) or (thisScreen == ScreenNames.CREATE_USER_SCREEN.value):
            self.gui.displayErrorMessageLoginS(errorCodes)
        if (thisScreen == ScreenNames.PROGRAMMING_SCREEN.value):
            self.gui.displayErrorMessageProgramS(errorCodes)

    def drawPacemakerData(self, readData):
        self.gui.displayPacemakerData(readData)

    def p_drawFirstScreen(self):
        """
        Draw first screen in application - in our case - login screen
        """
        self.drawScreen(loginScreen)

    def p_drawLoginScreen(self, data):
        """
        Draw screen of type login screen
        """
        self.gui.drawTwoFieldsTwoButtonLayout(
            data.fieldLabels, 
            data.buttonTexts, 
            data.buttonCallbacks)

    def p_drawProgrammingScreen(self, data):
        """
        Draw screen of type programming screen
        @param - data -> type = ProgramMenuData
        """
        # Get programming values
        programmingValues = data.getProgrammingValues()
        programMode = programmingValues.getProgramMode()
        textBoxStr = [
                C_PROGRAM_DATA_LABEL[0],
                str(C_PROGRAM_DATA_LABEL[1].format(programMode)),
                str(C_PROGRAM_DATA_LABEL[2].format(
                int(programmingValues.getUpperRateLimit()),
                int(programmingValues.getAtrialAmplitude()),
                int(programmingValues.getVentricularAmplitude()))),
                str(C_PROGRAM_DATA_LABEL[3].format(
                int(programmingValues.getLowerRateLimit()),
                int(programmingValues.getAtrialPulseWidth()),
                int(programmingValues.getVentricularPulseWidth()))),
                str(C_PROGRAM_DATA_LABEL[4].format(
                int(programmingValues.getAccelerationFactor()),
                int(programmingValues.getAtrialSensingThreshold()),
                int(programmingValues.getVentricularSensingThreshold()))),
                str(C_PROGRAM_DATA_LABEL[5].format(
                int(programmingValues.getFixedAVDelay()),        
                int(programmingValues.getAtrialRefractoryPeriod()),
                int(programmingValues.getVentricularRefractoryPeriod())))
                ]
        self.gui.drawNFieldsNButtonsOneDropDownLayout(
            data.dropDownLabelText, 
            programMode,
            data.dropDownOptions, 
            data.fieldLabels,
            data.buttonTexts,
            data.buttonCallbacks,
            textBoxStr)
 
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

    

    
