class ApplicationCallbacks:
    def __init__(self, loginButtonCB, logoffButtonCB, newUserButtonCB, createUserButtonCB, cancelButtonCB, programButtonCB):
        self.loginButtonCB = loginButtonCB
        self.logoffButtonCB = logoffButtonCB
        self.newUserButtonCB = newUserButtonCB
        self.createUserButtonCB = createUserButtonCB
        self.cancelButtonCB = cancelButtonCB
        self.programButtonCB = programButtonCB
        # self.changeProgramModeCB = changeProgramModeCB