class ApplicationCallbacks:
    def __init__(self, loginButtonCB, logoffButtonCB, newUserButtonCB, programButtonCB, changeProgramModeCB,createUserButtonCB,cancelButtonCB):
        self.loginButtonCB = loginButtonCB
        self.logoffButtonCB = logoffButtonCB
        self.newUserButtonCB = newUserButtonCB
        self.programButtonCB = programButtonCB
        self.changeProgramModeCB = changeProgramModeCB
        self.createUserButtonCB = createUserButtonCB
        self.cancelButtonCB = cancelButtonCB