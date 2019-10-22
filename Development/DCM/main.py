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
        print(self.accountController.signInUser(self.guiController.getLoginData()).value)
        #self.guiController.drawScreen(programmingScreen)

    def logoffButtonCB(self):
        self.guiController.drawScreen(loginScreen)

    def newUserButtonCB(self):
        self.guiController.drawScreen(createUserScreen)

    def createUserButtonCB(self):
        x = self.accountController.makeNewUser(self.guiController.getNewUserData(),"hello")
        print(x)
        if x.value == 0:
            self.guiController.drawScreen(programmingScreen)

    def cancelButtonCB(self):
        self.guiController.drawScreen(loginScreen)


def main():
    #print(hash_password('hello')) #Displays hashed Admin password

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


    callbacks = ApplicationCallbacks(loginButtonCallback, logoffButtonCallback, newUserButtonCallback, None, None,createUserButtonCallback,cancelButtonCallback)

    app.setCallbacks(callbacks)

    # Start GUI - open first window
    app.startGUI()     

    while 1:
        app.updateGUI()
        time.sleep(0.01)
main()