# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from DCMGraphicalUserInterface.guic import *
from DCMUserAccountManager.duam     import *
import time


def main():
    sessionController = DUAM()   # Init session controller - handles user sessions
    guiController = GUIC()       # Init GUI controller
    guiController.updateGUI()    # Update GUI
    while 1:
        guiController.updateGUI()
        time.sleep(0.01)
main()