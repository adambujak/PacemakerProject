# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
from Common.callbacks               import ApplicationCallbacks
import time



def loginButtonCallback():
    print("button cl")

def newUserButtonCallback():
    print("new user button click")

callbacks = ApplicationCallbacks(loginButtonCallback, newUserButtonCallback,None, None)

def main():
    accountController = DUAM()         # Init session controller - handles user sessions
    guiController = GUIC(callbacks)    # Init GUI controller
    guiController.updateGUI()          # Update GUI

    while 1:
        guiController.updateGUI()
        time.sleep(0.01)
main()