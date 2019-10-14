class ApplicationCallbacks:
    def __init__(self, loginButtonCB, newUserButtonCB, programButtonCB, changeProgramModeCB):
        self.loginButtonCB = loginButtonCB
        self.newUserButtonCB = newUserButtonCB
        self.programButtonCB = programButtonCB
        self.changeProgramModeCB = changeProgramModeCB