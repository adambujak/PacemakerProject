# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: Main Application Source File
# Filename: main.py

from GUIC.guic import *

def main():
    guiController = GUIC()
    guiController.updateGUI()
    input()
main()