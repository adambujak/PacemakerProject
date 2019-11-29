# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *
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

    def getPacemakerParameterData(self, data):
        """
        Retrieves data from gui input fields on Programming Screen
        """
        if self.currentScreen.screenName == ScreenNames.PROGRAMMING_SCREEN:
            programMode = data.getProgrammingValues().getProgramModeInt();
            entryData = self.gui.getEntryData()
            for entryIndex in range(len(entryData)):
                if entryData[entryIndex] == '':
                    entryData[entryIndex] = -1;
                else:
                    entryData[entryIndex] = float(entryData[entryIndex]);
            if programMode == 0 or programMode == 1:
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], entryData[2], entryData[3], entryData[4], entryData[5], 0, 0, 0, 0, 0, 0, 0)
            elif programMode == 2 or programMode == 3:
                    return PacemakerParameterData(programMode, entryData[0], entryData[1], 0, 0, 0, 0, entryData[2], entryData[3], entryData[4], entryData[5], 0, 0, 0)
        
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
        fLabels = list(data.fieldLabels)
        programMode = programmingValues.getProgramMode()
        textBoxStr = [
        "\t\t\t\t\tValues currently stored in Database:\n",
        "\t\t\t\t\tProgram Mode: {}                             ",
        "\tUpper Rate Limit: {} BPM,\t\tAtrial Amplitude: {} mV,\t\tVentricular Amplitude: {} mV\n",
        "\tLower Rate Limit: {} BPM,\t\tAtrial Pulse Width: {} ms,\t\t\tVentricular Pulse Width: {} ms\n",
        "\tModulation Sensitivity: {},\t\tAtrial Sensing Threshold: {} mV,\t\tVentricular Sensing Threshold: {} mV\n",
        "\tAV Delay: {} ms,\t\t\tAtrial Refractory Period: {} ms,\t\tVentricular Refractory Period: {} ms"
        ]
        textBoxStr[1] = textBoxStr[1].format(
                programmingValues.getProgramMode()
                )
        textBoxStr[2] = textBoxStr[2].format(
                programmingValues.getUpperRateLimit(),
                programmingValues.getAtrialAmplitude(),
                programmingValues.getVentricularAmplitude()
                )
        textBoxStr[3] = textBoxStr[3].format(
                programmingValues.getLowerRateLimit(),
                programmingValues.getAtrialPulseWidth(),
                programmingValues.getVentricularPulseWidth()
                )
        textBoxStr[4] = textBoxStr[4].format(
                programmingValues.getAccelerationFactor(),
                programmingValues.getAtrialSensingThreshold(),
                programmingValues.getAtrialRefractoryPeriod()
                )
        textBoxStr[5] = textBoxStr[5].format(
                programmingValues.getFixedAVDelay(),        
                programmingValues.getVentricularSensingThreshold(),
                programmingValues.getVentricularRefractoryPeriod()
                )
        print(textBoxStr)

        self.gui.drawNFieldsNButtonsOneDropDownLayout(
            data.dropDownLabelText, 
            programMode,
            data.dropDownOptions, 
            fLabels,
            data.buttonTexts,
            data.buttonCallbacks,
            textBoxStr)

        # # Make list of programming values
        # if programMode == "AOO" or programMode == "AAI":
        #     programmingValuesList = [
        #         programmingValues.getUpperRateLimit(),
        #         programmingValues.getLowerRateLimit(),
        #         programmingValues.getAtrialAmplitude(),
        #         programmingValues.getAtrialPulseWidth(),
        #         programmingValues.getAtrialSensingThreshold(),
        #         programmingValues.getAtrialRefractoryPeriod(),
        #         ]
        # elif programMode == "VOO" or programMode == "VVI":
        #     programmingValuesList = [
        #         programmingValues.getUpperRateLimit(),
        #         programmingValues.getLowerRateLimit(),
        #         programmingValues.getVentricularAmplitude(),
        #         programmingValues.getVentricularPulseWidth(),
        #         programmingValues.getVentricularSensingThreshold(),
        #         programmingValues.getVentricularRefractoryPeriod(),
        #         ]
        #self.gui.setNEntryData(programmingValuesList)

    def p_drawErrorMessageOnScreen(self, errorCode, thisScreen):
        if (thisScreen == ScreenNames.LOGIN_SCREEN.value) or (thisScreen == ScreenNames.CREATE_USER_SCREEN.value):
            self.gui.displayErrorMessageLoginS(errorCode)

    def p_drawErrorMessageProgramScreen(self, errorCodeRate, errorCodeChamber, thisScreen):
        if (thisScreen == ScreenNames.PROGRAMMING_SCREEN.value):
            self.gui.displayErrorMessageProgramS(errorCodeRate, errorCodeChamber)

 
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

    

    
