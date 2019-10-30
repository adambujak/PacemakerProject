# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
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
        programmedData = self.guiController.getUserProgramData() #will return all the
        # print ("user program data on program button callback")
        # programmedData.printData()
        stateRateLim = self.accountController.programRateLim(programmedData.upperRateLimit, programmedData.lowerRateLimit)
        stateAtriaPara = self.accountController.programAtriaPara(programmedData.atrialAmplitude, programmedData.atrialPulseWidth, 
                programmedData.atrialSensingThreshold, programmedData.atrialRefractoryPeriod)
        stateVentriclePara = self.accountController.programVentriclePara(programmedData.ventricularAmplitude, programmedData.ventricularPulseWidth,
                programmedData.ventricularSensingThreshold,programmedData.ventricularRefractoryPeriod)
        if ((stateRateLim.value == 0)
            and (stateVentriclePara.value == 0)
            and (stateVentriclePara.value == 0)):
            self.accountController.saveProgrammingValuesToDatabase()
            self.guiController.drawScreen(programmingScreen)
        self.guiController.p_drawErrorMessageProgramScreen(stateRateLim.name, stateAtriaPara.name, stateVentriclePara.name, 1)



def main():
    #print(hash_password("C_ADMIN_PASSWORD")) #Displays hashed C_ADMIN_PASSWORD

    app = MainApplication()


    callbacks = ApplicationCallbacks(
        app.loginButtonCB, 
        app.logoffButtonCB, 
        app.newUserButtonCB,
        app.createUserButtonCB, 
        app.cancelButtonCB, 
        app.programButtonCB, 
        None)

    app.setCallbacks(callbacks)

    # Start GUI - open first window
    app.startGUI()     

    while 1:
        app.updateGUI()
        time.sleep(0.01)
main()