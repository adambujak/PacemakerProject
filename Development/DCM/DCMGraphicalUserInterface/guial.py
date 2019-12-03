# Author: Adam Bujak
# Date Created: Thurdsay, September 26, 2019
# Description: GUI Abstraction Layer Source File
# Filename: guial.py


import tkinter as tk
from src.dcm_constants import *
from Common.failCodes  import FailureCodes


#############################################################
############### GUI Abstraction Layer Class #################
#############################################################



class GUIAL:
    # root = Tk()
    # img = ImageTk.PhotoImage(Image.open("True1.gif"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    # root.mainloop()

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
        self.instance.geometry("350x125")
        print("Started Two Fields One Button Layout")
        self.instance.title(self.title)

        #self.instance.configure(background = "grey");

        #Attempt to add logo to GUI Upper right corner of Login Screen
        # img = tk.PhotoImage(file="logoMac.gif")
        # label = Label(image=photo)
        # img.image = img
        # panel = tk.Label(self.instance, image = img).grid(row = 0,column = 0)
        # panel.pack(side = "bottom", fill = "both", expand = "yes").    

        a = tk.Label(self.instance ,text = fieldLabels[0]).grid(row = 0,column = 1)
        b = tk.Label(self.instance ,text = fieldLabels[1]).grid(row = 1,column = 1)

        a1 = tk.Entry(self.instance).grid(row = 0,column = 2)
        b1 = tk.Entry(self.instance).grid(row = 1,column = 2)

        btn = tk.Button(self.instance ,text=buttonTexts[0], command = buttonCallbacks[0]).grid(row=2,column=2)
        btn = tk.Button(self.instance ,text=buttonTexts[1], command = buttonCallbacks[1]).grid(row=3,column=2)

    def drawNFieldsNButtonsOneDropDownLayout(self, dropDownLabelText, currentDropDownItem, dropDownOptions, fieldLabels, buttonTexts, buttonCallbacks, dataStr):
        """Draws Program Screen acrroding to current programMode
        Params:
        dropDownLabelText    - Label for dropDownMenu, Title
        currentDropDownItem  - Value of current dropDownOption, current program mode
        dropDownOptions      - Set of dropDownOptions, List of all programmable modes
        fieldLabels          - Array of labels for input fields, All relevant programmable variables
        buttonText           - Text to be displayed in buttons, program and quit buttin text
        buttonCallback       - Button callback function, programButtonCB and cancelButtonCB
        """
        self.guiInitialized = True
        self.instance.title(self.title)
        #self.instance.configure(background = "white");
        self.instance.geometry("790x440")
        self.instance.grid_rowconfigure(0, minsize=25)
        self.instance.grid_rowconfigure(10, minsize=25)
        self.instance.grid_columnconfigure(9, minsize=25)
        print('Program Screen')
        rowLabel = 11
        for row in range(len(dataStr)):
            tk.Label(self.instance, text = dataStr[row], anchor="w", bg="white").grid(sticky="w", row= rowLabel + row, column=0, columnspan=15)
        tk.Label(self.instance, text=dropDownLabelText).grid(row = 1, column = 3)
        if not currentDropDownItem in dropDownOptions:
            print("ERROR: Invalid dropDownOption")
            return
        else:
            self.programMode = currentDropDownItem
        valCheckBox = tk.BooleanVar(self.instance)
        tkvar = tk.StringVar(self.instance)
        tkvar.set(self.programMode) 
        if dropDownOptions.index(self.programMode) <= 4:
            valCheckBox.set(False)
            programList = list(dropDownOptions[0:5])
        else:
            valCheckBox.set(True)
            programList = list(dropDownOptions[5:10])
        
        def changeModeCB(programMode):
            self.programMode = programMode
            self.displayLabelEntry(self.programMode, dropDownOptions, fieldLabels)

        def changeCheckCB():
            if valCheckBox.get():
                self.programMode = dropDownOptions[dropDownOptions.index(self.programMode)+5]
                programList = list(dropDownOptions[5:10])
            else:
                self.programMode = dropDownOptions[dropDownOptions.index(self.programMode)-5]
                programList = list(dropDownOptions[0:5])
            tkvar.set(self.programMode)
            for wig in self.instance.grid_slaves():
                rowVal = int(wig.grid_info().get("row"))
                colVal = int(wig.grid_info().get("column"))
                if rowVal ==2 and colVal == 3:
                    wig.destroy()
                    break
            popupMenu = tk.OptionMenu(self.instance, tkvar, *programList, command = changeModeCB).grid(row = 2, column = 3)
            changeModeCB(self.programMode)       

        checkBox = tk.Checkbutton(self.instance, text="Rate Modulation", variable=valCheckBox, command = changeCheckCB).grid(row = 2, column = 4)       
        popupMenu = tk.OptionMenu(self.instance, tkvar, *programList, command = changeModeCB).grid(row = 2, column = 3)
        changeModeCB(self.programMode)

        for buttonIndex in range(3):         # Draw each button
            btn = tk.Button(self.instance , text=buttonTexts[buttonIndex], command = buttonCallbacks[buttonIndex]).grid(row = (buttonIndex + 7), column = 3)

    def displayLabelEntry(self, programMode, dropDownOptions, fieldLabels):
        for wig in self.instance.grid_slaves():
            rowVal = int(wig.grid_info().get("row"))
            colVal = int(wig.grid_info().get("column"))
            if rowVal >= 3 and rowVal <= 6:
                wig.destroy()
            if rowVal == 7 and (colVal == 2 or colVal == 4 or colVal == 6):
                wig.destroy()
        if programMode == dropDownOptions[0] or programMode == dropDownOptions[1]:
            # self.instance.geometry("550x275")
            fieldInd = [[0,1], [0,1], [0,1,2,3]]
        if programMode == dropDownOptions[2] or programMode == dropDownOptions[3]:
            # self.instance.geometry("550x275")
            fieldInd = [[0,2], [0,1], [0,1,2,3]]
        if programMode == dropDownOptions[4]:
            # self.instance.geometry("800x275")
            fieldInd = [[0,1,2], [0,1,3], [0,1,2,3], [0,1,2,3]]
        if programMode == dropDownOptions[5] or programMode == dropDownOptions[6]:
            # self.instance.geometry("550x275")
            fieldInd = [[0,1], [0,1,2], [0,1,2,3]]
        if programMode == dropDownOptions[7] or programMode == dropDownOptions[8]:
            # self.instance.geometry("550x275")
            fieldInd = [[0,2], [0,1,2], [0,1,2,3]]
        if programMode == dropDownOptions[9]:
            # self.instance.geometry("800x275")
            fieldInd = [[0,1,2], [0,1,2,3], [0,1,2,3], [0,1,2,3]]
        colOffset = 1
        for columns in fieldInd[0]:
            rowOffset = 3
            for field in fieldInd[int(colOffset/2)+1]:
                label = tk.Label(self.instance, text = fieldLabels[columns][field], anchor="e").grid(sticky="E", row = rowOffset, column = colOffset)
                entry = tk.Entry(self.instance).grid(row = rowOffset, column = colOffset + 1)
                rowOffset +=1
            colOffset +=2

    def getProgramMode(self):
        return self.programMode

    def displayErrorMessageLoginS(self, errorCode):
        label = tk.Label(self.instance, text = errorCode.name, bg = "red").grid(row = 0, column = 3)

    def displayErrorMessageProgramS(self, errorCodes):
        for wig in self.instance.grid_slaves():
            rowVal = int(wig.grid_info().get("row"))
            colVal = int(wig.grid_info().get("column"))
            if rowVal == 7 and (colVal == 2 or colVal == 4 or colVal == 6):
                wig.destroy()
            if rowVal == 7 and (colVal == 2 or colVal == 4 or colVal == 6):
                wig.destroy()
            # if rowVal == 7 and colVal == 4:
            #     wig.destroy()
        if errorCodes[0] != 11 or errorCodes[0] != 10:
            for i in range(1,len(errorCodes)):
                if errorCodes[i].value == 0:
                    label = tk.Label(self.instance, text = errorCodes[i].name, bg = "green").grid(row = 7, column = 2*i)
                else:
                    label = tk.Label(self.instance, text = errorCodes[i].name, bg = "red").grid(row = 7, column = 2*i)
        if errorCodes[0] == 11:
            label = tk.Label(self.instance, text = "Successfully programed PaceMaker", bg = "green").grid(sticky="W",row = 7, column = 4, columnspan = 6)
        if errorCodes[0] == 10:
            label = tk.Label(self.instance, text = "Could not program PaceMaker", bg = "red").grid(sticky="W",row = 7, column = 4, columnspan = 6)

    def displayPacemakerData(self, readData):
        rowLabel = 17
        for row in range(len(dataStr)):
            tk.Label(self.instance, text = dataStr[row], anchor="w", bg="white").grid(sticky="w", row= rowLabel + row, column=0, columnspan=15)
        self.instance.geometry("790x600")

    def getEntryData(self):
        children = self.instance.winfo_children()
        output = []
        for item in children:
            if type(item) == tk.Entry:
                output.append(item.get())
        return output

    def setNEntryData(self, data):
        """Sets each entry to value in data array
            @param data - array of values to be set
        """
        children = self.instance.winfo_children()
        itemCnt = 0;
        for item in children:
            if type(item) == tk.Entry:
                if itemCnt >= len(data):
                    return
                #print("Data[itemCnt]", data[itemCnt])
                item.delete(0, tk.END)
                item.insert(0, data[itemCnt])
                itemCnt += 1;



