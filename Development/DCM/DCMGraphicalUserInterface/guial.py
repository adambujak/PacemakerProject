# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Abstraction Layer Source File
# Filename: guial.py


import tkinter as tk
from src.dcm_constants import *


#############################################################
############### GUI Abstraction Layer Class #################
#############################################################

class GUIAL:

    # Initialize GUI Abstraction Layer #
    def __init__(self):
        self.instance = tk.Tk()
        self.guiInitialized = False

    # Initialize GUI #
    def initGUI(self):
        w = tk.Label(self.instance, text = C_INTRO_TEXT)
        w.pack()

        self.instance.update()

        self.guiInitialized = True
        print("Initialized GUI")

    # Update GUI #
    def update(self):
        # If GUI hasn't been initialized, initialize it #
        if self.guiInitialized == False:
            self.initGUI()

        self.instance.update()

