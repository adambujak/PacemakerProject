class PacemakerParameterData:
    def __init__(self, p_programMode, p_upperRateLimit, p_lowerRateLimit, 
        p_atrialAmplitude, p_atrialPulseWidth, p_atrialSensingThreshold, p_atrialRefractoryPeriod, 
        p_ventricularAmplitude, p_ventricularPulseWidth, p_ventricularSensingThreshold, p_ventricularRefractoryPeriod,
        p_fixedAVDelay, p_modulationSensitivity, p_rateModulation):
        self.programMode                  = p_programMode
        self.lowerRateLimit               = p_lowerRateLimit
        self.upperRateLimit               = p_upperRateLimit
        self.atrialAmplitude              = p_atrialAmplitude
        self.atrialPulseWidth             = p_atrialPulseWidth
        self.atrialSensingThreshold       = p_atrialSensingThreshold
        self.atrialRefractoryPeriod       = p_atrialRefractoryPeriod
        self.ventricularAmplitude         = p_ventricularAmplitude
        self.ventricularPulseWidth        = p_ventricularPulseWidth
        self.ventricularSensingThreshold  = p_ventricularSensingThreshold
        self.ventricularRefractoryPeriod  = p_ventricularRefractoryPeriod
        self.fixedAVDelay                 = p_fixedAVDelay
        self.modulationSensitivity        = p_modulationSensitivity
        self.rateModulation               = p_rateModulation

    def getProgramModeInt(self):
        if self.programMode == 'AOO':
            return 0
        if self.programMode == 'VOO':
            return 1
        if self.programMode == 'AAI':
            return 2
        if self.programMode == 'VVI':
            return 3
        if self.programMode == 'DOO':
            return 4
        if self.programMode == 'AOOR':
            return 5
        if self.programMode == 'VOOR':
            return 6
        if self.programMode == 'AAIR':
            return 7
        if self.programMode == 'VVIR':
            return 8
        if self.programMode == 'DOOR':
            return 9

    def getProgramModeFromInt(self):
        if self.programMode == 0:
            return 'AOO'
        if self.programMode == 1:
            return 'VOO'
        if self.programMode == 2:
            return 'AAI'
        if self.programMode == 3:
            return 'VVI'
        if self.programMode == 4:
            return 'DOO'
        if self.programMode == 5:
            return 'AOOR'
        if self.programMode == 6:
            return 'VOOR'
        if self.programMode == 7:
            return 'AAIR'
        if self.programMode == 8:
            return 'VVIR'
        if self.programMode == 9:
            return 'DOOR'

    def getProgramMode(self):
        return self.programMode   
    def getLowerRateLimit(self):
        return self.lowerRateLimit
    def getUpperRateLimit(self):
        return self.upperRateLimit
    def getAtrialAmplitude(self):
        return self.atrialAmplitude
    def getAtrialAmplitudeInMV(self):
        return int(self.atrialAmplitude)
    def getAtrialPulseWidth(self):
        return self.atrialPulseWidth
    def getAtrialSensingThreshold(self):
        return self.atrialSensingThreshold
    def getAtrialSensingThresholdInMV(self):
        return int(self.atrialSensingThreshold)
    def getAtrialRefractoryPeriod(self):
        return self.atrialRefractoryPeriod
    def getVentricularAmplitude(self):
        return self.ventricularAmplitude
    def getVentricularAmplitudeInMV(self):
        return int(self.ventricularAmplitude)
    def getVentricularPulseWidth(self):
        return self.ventricularPulseWidth
    def getVentricularSensingThreshold(self):
        return self.ventricularSensingThreshold
    def getVentricularSensingThresholdInMV(self):
        return int(self.ventricularSensingThreshold)
    def getVentricularRefractoryPeriod(self):
        return self.ventricularRefractoryPeriod
    def getFixedAVDelay(self):
        return self.fixedAVDelay
    def getAccelerationFactor(self):
        return self.modulationSensitivity
    def getRateModulation(self):
        return self.rateModulation


    def setProgramMode(self,val):
        self.programMode=val
    def setLowerRateLimit(self,val):
        self.lowerRateLimit=val
    def setUpperRateLimit(self,val):
        self.upperRateLimit=val
    def setAtrialAmplitude(self,val):
        self.atrialAmplitude=val
    def setAtrialPulseWidth(self,val):
        self.atrialPulseWidth=val
    def setAtrialSensingThreshold(self,val):
        self.atrialSensingThreshold=val
    def setAtrialRefractoryPeriod(self,val):
        self.atrialRefractoryPeriod=val
    def setVentricularAmplitude(self,val):
        self.ventricularAmplitude=val
    def setVentricularPulseWidth(self,val):
        self.ventricularPulseWidth=val
    def setVentricularSensingThreshold(self,val):
        self.ventricularSensingThreshold=val
    def setVentricularRefractoryPeriod(self,val):
        self.ventricularRefractoryPeriod=val
    def setFixedAVDelay(self,val):
        self.fixedAVDelay=val
    def setAccelerationFactor(self,val):
        self.modulationSensitivity=val
    def setRateModulation(self,val):
        self.rateModulation=val

    def printData(self):
        print("User Program Data", 
            "\nprogram mode: ", self.programMode,                
            "\nlowerRateLimit: ", self.lowerRateLimit,             
            "\nupperRateLimit: ", self.upperRateLimit,             
            "\natrialAmplitude: ", self.atrialAmplitude,            
            "\natrialPulseWidth: ", self.atrialPulseWidth,           
            "\natrialSensingThreshold: ", self.atrialSensingThreshold,     
            "\natrialRefractoryPeriod: ", self.atrialRefractoryPeriod,     
            "\nventricularAmplitude: ", self.ventricularAmplitude,       
            "\nventricularPulseWidth: ", self.ventricularPulseWidth,      
            "\nventricularSensingThreshold: ", self.ventricularSensingThreshold,
            "\nventricularRefractoryPeriod: ", self.ventricularRefractoryPeriod,
            "\nfixedAVDelay: ", self.fixedAVDelay,               
            "\nmodulationSensitivity: ", self.modulationSensitivity,      
            "\nrateModulation: ", self.rateModulation
            )             
