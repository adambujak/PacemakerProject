class ApplicationCallbacks:
    def __init__(self, loginButtonCB, logoffButtonCB, newUserButtonCB, programButtonCB, changeProgramModeCB):
        self.loginButtonCB = loginButtonCB
        self.logoffButtonCB = logoffButtonCB
        self.newUserButtonCB = newUserButtonCB
        self.programButtonCB = programButtonCB
        self.changeProgramModeCB = changeProgramModeCB