# Author: Adam Bujak
# Date Created: Tuesday, November 19, 2019
# Description: DCM Communication Controller
# Filename: dcc.py

from DCMSerial.dsm     import *
from src.dcm_constants import *
from Common.datatypes  import *
from struct            import *


#############################################################
############   DCM Communication Controller   ###############
#############################################################
#from Development.DCM.src.dcm_constants import C_SERIAL_ACK_RECEIVE_STRING


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
        prepend = bytearray([C_SERIAL_START_BYTE])
        return prepend + data

    def p_transmitData(self, data):
        '''
        @brief  Sends pacemaker data using DCM Serial Manager
        @param  data    - data to be sent
        @retval success - True/False
        '''
        data = self.p_prependDataWithStartCode(data)
        self.serialManager.write(data)
        
        received = self.serialManager.readLine()
        if received == FailureCodes.CANNOT_OPEN_COM_PORT:
            print("Cannot Transmit Data")
            return FailureCodes.CANNOT_OPEN_COM_PORT
        return True

    def programPacemaker(self, params):
        '''
        @brief  Sends pacemaker programmable parameters
        @param  params  - programmable parameters
        @retval success - True/False
        '''
        params = self.p_convertPacemakerParamsToByteArray(params)
        if (self.p_transmitData(params) == True):
            return True
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
        transferList += (self.p_convertToInts(pacemakerParams.getProgramModeInt(),                  1))
        transferList += (self.p_convertToInts(pacemakerParams.lowerRateLimit,                       1))
        transferList += (self.p_convertToInts(pacemakerParams.upperRateLimit,                       1))
        transferList += (self.p_convertToInts(pacemakerParams.getAtrialAmplitudeInMV(),             2))
        transferList += (self.p_convertToInts(pacemakerParams.getVentricularAmplitudeInMV(),        2))
        transferList += (self.p_convertToInts(pacemakerParams.atrialPulseWidth,                     1))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularPulseWidth,                1))
        transferList += (self.p_convertToInts(pacemakerParams.getAtrialSensingThresholdInMV(),      2))
        transferList += (self.p_convertToInts(pacemakerParams.getVentricularSensingThresholdInMV(), 2))
        transferList += (self.p_convertToInts(pacemakerParams.atrialRefractoryPeriod,               2))
        transferList += (self.p_convertToInts(pacemakerParams.ventricularRefractoryPeriod,          2))
        transferList += (self.p_convertToInts(pacemakerParams.fixedAVDelay,                         2))
        transferList += (self.p_convertToInts(pacemakerParams.rateModulation,                       1))
        transferList += (self.p_convertToInts(pacemakerParams.modulationSensitivity,                1))
        byteArray = bytearray(transferList)
        return byteArray

    def p_sendEchoCommand(self):
        '''
        @brief  Sends echo command to pacemaker
        @param  None
        @retval success - True/False
        '''
        sendBuffer = pack(C_SERIAL_PARAMETER_ECHO_PACK, C_SERIAL_START_BYTE, C_SERIAL_ECHO_COMMAND_BYTE)
        return self.serialManager.write(sendBuffer)

    def p_convertArrayToPacemakerData(self, array):
        '''
        @brief  Converts array into pacemaker data type
        @param  array   - array to be converted
        @retval data    - pacemaker data
        '''
        return PacemakerParameterData(
            p_programMode                 = array[0],
            p_lowerRateLimit              = array[1],
            p_upperRateLimit              = array[2],
            p_atrialAmplitude             = array[3],
            p_ventricularAmplitude        = array[4],
            p_atrialPulseWidth            = array[5],
            p_ventricularPulseWidth       = array[6],
            p_atrialSensingThreshold      = array[7],
            p_ventricularSensingThreshold = array[8],
            p_atrialRefractoryPeriod      = array[9],
            p_ventricularRefractoryPeriod = array[10],
            p_fixedAVDelay                = array[11],
            p_rateModulation              = array[12],
            p_modulationSensitivity       = array[13]
            )

    def getPacemakerData(self):
        '''
        @brief  Get parameters stored on pacemaker
        @param  None
        @retval Pacemaker Data - in array
        '''
        validData = False
        while not validData:
            sent = self.p_sendEchoCommand()
            if (sent == True):
                while self.serialManager.hSerial.in_waiting < C_SERIAL_PARAMETER_BYTE_CNT:
                    pass
                readData = self.serialManager.read(C_SERIAL_PARAMETER_BYTE_CNT)
                readData = unpack(C_SERIAL_PARAMETER_ECHO_UNPACK, readData)
                for i in readData:
                    if i != 0:
                        return self.p_convertArrayToPacemakerData(readData)
            if (sent == FailureCodes.CANNOT_OPEN_COM_PORT):
                return False
        return None

    def p_sendGetEgram(self):
        '''
        @brief  Sends echo egram values command to pacemaker
        @param  None
        @retval success - True/False
        '''
        sendBuffer = pack(C_SERIAL_EGRAM_ECHO_PACK, C_SERIAL_START_BYTE, C_SERIAL_EGRAM_START_BYTE)
        return self.serialManager.write(sendBuffer)
    
    def getElectrogram(self):
        '''
        @brief  Reads electrogram from pacemaker
        @param  None
        @retval Array of electrogram values
        '''
        while self.serialManager.hSerial.in_waiting < C_SERIAL_PARAMETER_BYTE_CNT:
            pass
        self.egramRead = self.serialManager.read(C_SERIAL_PARAMETER_BYTE_CNT)
        

