# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
from Common.callbacks               import ApplicationCallbacks
import time



class MainApplication:
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
            self.guiController.drawScreen(programmingScreen)
        else:
            print(stateCode.name)
        print(self.accountController.getSessionState())


    def logoffButtonCB(self):
        if self.accountController.signOut():
            self.guiController.drawScreen(loginScreen)

    def newUserButtonCB(self):
        self.guiController.drawScreen(createUserMenuScreen)

    def createUserButtonCB(self):
        stateCode = self.accountController.makeNewUser(self.guiController.getNewUserData(),"C_ADMIN_PASSWORD")
        if  stateCode.value == 0:
            self.guiController.drawScreen(programmingScreen)
        else:
            print(stateCode.name)

    def cancelButtonCB(self):
        self.guiController.drawScreen(loginScreen)

    def programButtonCB(self):
        #do user field restrictions in DUAM set functions "program...."
        programmedData = self.guiController.getProgramData() #will return all the
        parameterStatusR = self.accountController.programRateLim(programmedData)
        if parameterStatusR.value == 0:
            parameterStatusA = self.accountController.programAtriaPara(programmedData)
            if parameterStatusA.value == 0:
                parameterStatusV = self.accountController.programVentriclePara(programmedData)
                if parameterStatusV.value == 0:
                    self.guiController.drawScreen(programmingScreen)
                else:
                    print(parameterStatusV.name)
            else:
                print(parameterStatusA.name)
        else:
            print(parameterStatusR.name)



def main():
    #print(hash_password("C_ADMIN_PASSWORD")) #Displays hashed C_ADMIN_PASSWORD

    app = MainApplication()

    def loginButtonCallback():
        app.loginButtonCB()

    def logoffButtonCallback():
        app.logoffButtonCB()

    def newUserButtonCallback():
        app.newUserButtonCB()

    def createUserButtonCallback():
        app.createUserButtonCB()

    def cancelButtonCallback():
        app.cancelButtonCB()

    def programButtonCallback():
        app.programButtonCB()


    callbacks = ApplicationCallbacks(loginButtonCallback, logoffButtonCallback, newUserButtonCallback, createUserButtonCallback, cancelButtonCallback, None, None)

    app.setCallbacks(callbacks)

    # Start GUI - open first window
    app.startGUI()     

    while 1:
        app.updateGUI()
        time.sleep(0.01)
main()