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

    # Update GUI #
    def update(self):
        # If GUI hasn't been initialized, initialize it #
        if self.guiInitialized == False:
            return;

        self.instance.update()

    def setTitle(self, title):
        self.title = title;
        if self.guiInitialized == True:
            self.instance.title(self.title)

    def drawTwoFieldsOneButtonLayout(self, fieldLabel1, fieldLabel2, buttonText, buttonCallback ):
        """
        Draws two user input fields and a button to the screen
        Params:
        fieldLabel1    - Label for first input field
        fieldLabel2    - Label for second input field
        buttonText     - Text to be displayed in button
        buttonCallback - Button callback function 
        """
        self.guiInitialized = True
        print("Started Two Fields One Button Layout")
        self.instance.title(self.title)

        self.instance.configure(background = "white");

        a = tk.Label(self.instance ,text = fieldLabel1).grid(row = 0,column = 0)
        b = tk.Label(self.instance ,text = fieldLabel2).grid(row = 1,column = 0)
        a1 = tk.Entry(self.instance).grid(row = 0,column = 1)
        b1 = tk.Entry(self.instance).grid(row = 1,column = 1)

        btn = tk.Button(self.instance ,text=buttonText, command = buttonCallback).grid(row=5,column=1)

    def drawNFieldsOneButtonOneDropDownLayout(self, dropDownLabelText, currentDropDownItem, dropDownOptions, fieldLabels, buttonText, buttonCallback):
        """
        Draws two user input fields and a button to the screen
        Params:
        dropDownLabelText    - Label for dropDownMenu  
        currentDropDownItem  - Value of current dropDownOption
        dropDownOptions      - Set of dropDownOptions
        fieldLabels          - Array of labels for input fields
        buttonText           - Text to be displayed in button
        buttonCallback       - Button callback function 
        """

        self.guiInitialized = True
        print("Started Two Fields One Button Layout")

        self.instance.title(self.title)

        self.instance.configure(background = "white");

        # Create a Tkinter variable
        tkvar = tk.StringVar(self.instance)


        # Check if currentDropDownItem is contained in options
        # If not - return because something has gone wrong
        if not currentDropDownItem in dropDownOptions:
            print("ERROR: Invalid dropDownOption")
            return

        # Set the current option
        tkvar.set(currentDropDownItem) 

        popupMenuRowIndex = 1
        popupMenu = tk.OptionMenu(self.instance, tkvar, *dropDownOptions)
        tk.Label(self.instance, text=dropDownLabelText).grid(row = popupMenuRowIndex, column = 1)
        popupMenu.grid(row = popupMenuRowIndex+1, column =1)

        # On change dropdown value
        def change_dropdown(*args):
            print( tkvar.get() )

        # Link function to change dropdown
        tkvar.trace('w', change_dropdown)

        # Set the row offest so the entries and labels don't overwrite the popup menu
        # +2 because of the number of elements previously
        rowOffset = popupMenuRowIndex+2;

        # Draw each field
        for field in range(len(fieldLabels)):
            label = tk.Label(self.instance, text = fieldLabels[field]).grid(row = field+rowOffset, column = 0)
            entry = tk.Entry(self.instance).grid(row = field+rowOffset,column = 1)
        

        # Draw button
        btn = tk.Button(self.instance ,text=buttonText, command = buttonCallback).grid(row=len(fieldLabels)+rowOffset,column=1)
