# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
from DCMSerial.dsm                  import *
from Common.callbacks               import ApplicationCallbacks
from Common.failCodes               import FailureCodes
import time



class MainApplication:      #All print statements in MainApplication can be used in a call to display on gui screens
    def __init__(self):
        self.accountController = DUAM()
        self.guiController = GUIC()

    def setCallbacks(self, callbacks):
        self.guiController.setCallbacks(callbacks)

    def startGUI(self):
        self.guiController.startGUI()

    def updateGUI(self):
        self.guiController.updateGUI()

    def loginButtonCB(self):
        stateCode = self.accountController.signInUser(self.guiController.getLoginData())
        if stateCode.value == 0:
            self.guiController.setProgrammingValues(self.accountController.getProgrammingValues())
            self.guiController.drawScreen(programmingScreen)
        else:
            self.guiController.p_drawErrorMessageOnScreen(stateCode.name,0)
        print(self.accountController.getSessionState())

    def logoffButtonCB(self):
        if self.accountController.signOut():
            self.guiController.drawScreen(loginScreen)

    def newUserButtonCB(self):
        self.guiController.drawScreen(createUserMenuScreen)

    def createUserButtonCB(self):
        stateCode = self.accountController.makeNewUser(self.guiController.getNewUserData(),"C_ADMIN_PASSWORD")
        if  stateCode.value == 0:
            self.guiController.drawScreen(loginScreen)
        else:
            self.guiController.p_drawErrorMessageOnScreen(stateCode.name,2)

    def cancelButtonCB(self):
        self.guiController.drawScreen(loginScreen)

    def programButtonCB(self):
        #do user field restrictions in DUAM set functions "program...."
        # can do the hardware hidden print where program... functions store the error function then a get will return the failureCode to main to be printed or displayed
        programMode = self.accountController.getProgrammingValues().getProgramMode()
        #print("in programButtonCB, programMode is:", programMode)
        programmedData = self.guiController.getPacemakerParameterData(programMode) #will return all the
        # print ("user program data on program button callback")
        # programmedData.printData()
        # Should all theses calls of the class UserProgramData be using gets?
        stateRateLim = self.accountController.programRateLim(programmedData.upperRateLimit, programmedData.lowerRateLimit)
        if programmedData.programMode == "AOO" or programmedData.programMode == "AAI":
            stateChamberPara = self.accountController.programAtriaPara(programmedData.atrialAmplitude, programmedData.atrialPulseWidth, 
                programmedData.atrialSensingThreshold, programmedData.atrialRefractoryPeriod)
        elif programmedData.programMode == "VOO" or programmedData.programMode == "VVI":
            stateChamberPara = self.accountController.programVentriclePara(programmedData.ventricularAmplitude, programmedData.ventricularPulseWidth,
                programmedData.ventricularSensingThreshold, programmedData.ventricularRefractoryPeriod)

        if ((stateRateLim.value == 0)
            and (stateChamberPara.value == 0)):
            self.accountController.saveProgrammingValuesToDatabase()
            self.guiController.drawScreen(programmingScreen)
        self.guiController.p_drawErrorMessageProgramScreen(stateRateLim.name, stateChamberPara.name, 1)

    def changeProgramModeCB(self, programMode):
        stateProgramMode = self.accountController.programProgramMode(programMode)
        if stateProgramMode.value == 0:
            self.accountController.saveProgrammingValuesToDatabase()
            self.guiController.drawScreen(programmingScreen)


def main():

    app = MainApplication()


    callbacks = ApplicationCallbacks(
        app.loginButtonCB, 
        app.logoffButtonCB, 
        app.newUserButtonCB,
        app.createUserButtonCB, 
        app.cancelButtonCB, 
        app.programButtonCB,
        app.changeProgramModeCB)

    app.setCallbacks(callbacks)

    # serialManager = DSM() 
    # 
    # while 1:
    #     out = input()
    #     serialManager.writeString(out)
    #     out = ""
    #     while (out != 'recieved'):
    #         out = serialManager.readLine()
    #         print(out)


    #Start GUI - open first window
    app.startGUI()     

    while 1:
        app.updateGUI()
        time.sleep(0.01)

main()