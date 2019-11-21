# Author: Adam Bujak
# Date Created: Tuesday, November 19, 2019
# Description: DCM Communication Controller
# Filename: dcc.py

from DCMSerial.dsm     import *
from src.dcm_constants import *
from Common.datatypes  import *


#############################################################
############   DCM Communication Controller   ###############
#############################################################

class DCC:

    def __init__(self):
        self.serialManager = DSM()
        self.serialManagerInitialized = True

    def deinit(self):
        '''
        @brief  Deinitialization function
        @param  None
        @retval None
        '''
        self.serialManager.deinit()
        self.serialManagerInitialized = False

    def openConnection(self):
        '''
        @brief  Closes serial connection
        @param  None
        @retval None
        '''
        self.serialManager = DSM()
        self.serialManagerInitialized = True

    def closeConnection(self):
        '''
        @brief  Closes serial connection
        @param  None
        @retval None
        '''
        self.serialManager.deinit()
        self.serialManagerInitialized = False


    def p_prependDataWithStartCode(self, data):
        '''
        @brief  Prepends Serial Com Start Byte to Bytearray
        @param  data    - data to be sent
        @retval data with prepended start byte
        '''
        prepend = bytearray(C_SERIAL_START_BYTE)
        return prepend + data

    def p_transmitData(self, data):
        '''
        @brief  Sends pacemaker data using DCM Serial Manager
        @param  data    - data to be sent
        @retval success - True/False
        '''
        data = self.p_prependDataWithStartCode(data)
        self.serialManager.write(data)
        timeout = 0
        # ToDo: Figure out a better way to do this
        while (timeout < C_SERIAL_ACK_RECIEVE_TIMEOUT):
            recieved = self.serialManager.readLine().decode('utf-8')
            if recieved == FailureCodes.CANNOT_OPEN_COM_PORT:
                print("Cannot Transmit Data")
                return
            if recieved.find(C_SERIAL_ACK_RECIEVE_STRING) != -1:
                print("ACK recieved")
                return True
            timeout += 1
        print("ACK not recieved")
        return False

    def programPacemaker(self, params):
        '''
        @brief  Sends pacemaker programmable parameters
        @param  params  - programmable parameters
        @retval success - True/False
        '''
        params = self.p_convertPacemakerParamsToByteArray(params)
        print(params)
        if (self.p_transmitData(params) == False):
            return False
        
        #ToDo: read back params to ensure proper programming
        
    def p_convertToInts(self, number, numberOfBytes):
        if number == None:
            number = 0
        number   = int(number)
        lowByte  = (number & 0xff)
        highByte = ((number >> 8) & 0xff)
        if (numberOfBytes == 1):
            return [lowByte]
        return [lowByte, highByte]

    def p_convertPacemakerParamsToByteArray(self, pacemakerParams):
        '''
        @brief  Converts Pacemaker Parameters to Byte Array
        @param  pacemakerParams  - programmable pacemaker parameters
        @retval bytearray of pacemaker parameters
        '''
        transferList = [C_SERIAL_PARAMETER_START_BYTE]
        transferList += (self.p_convertToInts(pacemakerParams.getProgramModeInt(),         1))
        transferList += (self.p_convertToInts(pacemakerParams.lowerRateLimit,              1))
        transferList += (self.p_convertToInts(pacemakerParams.upperRateLimit,              1))
        transferList += (self.p_convertToInts(pacemakerParams.atrialAmplitude,             2))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularAmplitude,        2))
        transferList += (self.p_convertToInts(pacemakerParams.atrialPulseWidth,            1))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularPulseWidth,       1))
        transferList += (self.p_convertToInts(pacemakerParams.atrialSensingThreshold,      2))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularSensingThreshold, 2))
        transferList += (self.p_convertToInts(pacemakerParams.atrialRefractoryPeriod,      2))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularRefractoryPeriod, 2))
        transferList += (self.p_convertToInts(pacemakerParams.fixedAVDelay,                2))
        transferList += (self.p_convertToInts(pacemakerParams.rateModulation,              1))
        transferList += (self.p_convertToInts(pacemakerParams.accelerationFactor,          1))
        print (transferList)
        byteArray = bytearray(transferList)

        return byteArray

    def p_sendEchoCommand(self):
        '''
        @brief  Sends echo command to pacemaker
        @param  None
        @retval success - True/False
        '''
        return self.p_transmitData(C_SERIAL_ECHO_COMMAND_BYTE)

    def getPacemakerData(self):
        '''
        @brief  Get parameters stored on pacemaker
        @param  None
        @retval Pacemaker Data - in byte array
        '''
        if (p_sendEchoCommand() == True):
            return self.serialManager.readLine()
        return None

    def getElectrogram(self):
        '''
        @brief  Reads electrogram from pacemaker
        @param  None
        @retval Array of electrogram values
        '''
        pass
        

