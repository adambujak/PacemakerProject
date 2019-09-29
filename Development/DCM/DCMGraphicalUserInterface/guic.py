# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Controller Source File
# Filename: guic.py


from DCMGraphicalUserInterface.guial import *

#############################################################
################### GUI Controller Class ####################
#############################################################

class GUIC:

    # Initialize GUI Controller #
    def __init__(self):
        self.gui = GUIAL()
        print("Initialized GUI Controller")
    
    # Draw Screen to GUI #
    def drawScreen(self, screen):
        # ToDo: implement screen object 
        pass

    # Update GUI #
    def updateGUI(self):
        self.gui.update()

    
