# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
from DCMCommunicationController.dcc import *
from Common.callbacks               import ApplicationCallbacks
import time



class MainApplication:      #All print statements in MainApplication can be used in a call to display on gui screens
    def __init__(self):
        self.accountController = DUAM()
        self.guiController = GUIC()
        self.comController = DCC()

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
            self.guiController.drawErrorMessage(stateCode,0)
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
            self.guiController.drawErrorMessage(stateCode,2)

    def cancelButtonCB(self):
        self.guiController.drawScreen(loginScreen)

    def programButtonCB(self):
        stateError = self.accountController.controlProgramData(self.guiController.getPacemakerParameterData())
        if stateError[0] == 1:
            self.accountController.saveProgrammingValuesToDatabase()
            programmedData = self.accountController.getProgrammingValues()
            self.guiController.setProgrammingValues(programmedData)
            self.guiController.drawScreen(programmingScreen)
            if self.comController.programPacemaker(programmedData):
                stateError = [11] #Successfully programed Pacemaker
            else: 
                stateError = [10] #Failed to program Pacemaker
            self.guiController.drawErrorMessage(stateError, 1)
        else:
            self.guiController.drawErrorMessage(stateError, 1)

    def echoButtonCB(self):
        readData = self.comController.getPacemakerData()
        if not(readData is None):
            print("hi")
            self.guiController.drawPacemakerData(readData)
        print("bye")



def main():

    app = MainApplication()


    callbacks = ApplicationCallbacks(
        app.loginButtonCB, 
        app.logoffButtonCB, 
        app.newUserButtonCB,
        app.createUserButtonCB, 
        app.cancelButtonCB, 
        app.programButtonCB,
        app.echoButtonCB)

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