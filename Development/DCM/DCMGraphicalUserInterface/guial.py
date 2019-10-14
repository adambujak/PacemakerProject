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

    def clearWindow(self):
        """
        Clears all elements in window
        """
        _list = self.instance.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        for item in _list:
            item.destroy()

    def drawTwoFieldsTwoButtonLayout(self, fieldLabels, buttonTexts, buttonCallbacks ):
        """
        Draws two user input fields and a button to the screen
        Params:
        fieldLabels     - Array of labels for input fields
        buttonTexts     - Array of texts to be displayed in button
        buttonCallbacks - Array of button callback functions
        """
        
        self.guiInitialized = True
        print("Started Two Fields One Button Layout")
        self.instance.title(self.title)

        self.instance.configure(background = "white");

        a = tk.Label(self.instance ,text = fieldLabels[0]).grid(row = 0,column = 0)
        b = tk.Label(self.instance ,text = fieldLabels[1]).grid(row = 1,column = 0)
        a1 = tk.Entry(self.instance).grid(row = 0,column = 1)
        b1 = tk.Entry(self.instance).grid(row = 1,column = 1)

        btn = tk.Button(self.instance ,text=buttonTexts[0], command = buttonCallbacks[0]).grid(row=2,column=1)
        btn = tk.Button(self.instance ,text=buttonTexts[1], command = buttonCallbacks[1]).grid(row=3,column=1)

    def drawNFieldsNButtonsOneDropDownLayout(self, dropDownLabelText, currentDropDownItem, dropDownOptions, fieldLabels, buttonTexts, buttonCallbacks):
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
        print("Started N Fields N Button One DropDown Layout")

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
        
        # Update row offset to be the row after the last field 
        rowOffset += field + 1

        # Draw each button
        for buttonIndex in range(len(buttonTexts)):
            btn = tk.Button(self.instance ,text=buttonTexts[buttonIndex], command = buttonCallbacks[buttonIndex]).grid(row = (buttonIndex +rowOffset),column=1)

