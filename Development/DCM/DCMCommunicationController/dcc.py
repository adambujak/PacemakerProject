# Author: Adam Bujak
# Date Created: Tuesday, November 19, 2019
# Description: DCM Communication Controller
# Filename: dcc.py

from DCMSerial         import *
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
        pass

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
            recieved = self.serialManager.readLine()
            if C_SERIAL_ACK_RECIEVE_STRING in recieved:
                return True
        return False

    def programPacemaker(self, params):
        '''
        @brief  Sends pacemaker programmable parameters
        @param  params  - programmable parameters
        @retval success - True/False
        '''
        params = self.p_convertPacemakerParamsToByteArray(params)
        if (self.p_transmitData(params) == False):
            return False
        
        #ToDo: read back params to ensure proper programming
        
        pass

    def p_convertPacemakerParamsToByteArray(self, pacemakerParams):
        '''
        @brief  Converts Pacemaker Parameters to Byte Array
        @param  pacemakerParams  - programmable pacemaker parameters
        @retval bytearray of pacemaker parameters
        '''
        pass

    def p_sendEchoCommand(self):
        '''
        @brief  Sends echo command to pacemaker
        @param  None
        @retval success - True/False
        '''
        return self.p_transmitData(C_SERIAL_ECHO_COMMAND_BYTE):

    def getPacemakerData(self):
        '''
        @brief  Get parameters stored on pacemaker
        @param  None
        @retval Pacemaker Data - in byte array
        '''
        if (p_sendEchoCommand() == True)
            return self.serialManager.readLine()
        return None

    def getElectrogram(self):
        '''
        @brief  Reads electrogram from pacemaker
        @param  None
        @retval Array of electrogram values
        '''
        

