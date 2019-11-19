# Author: Adam Bujak
# Date Created: Saturday, November 19, 2019
# Description: DCM Serial Manager
# Filename: dsm.py

import serial
from src.dcm_constants import *


#############################################################
#################    DCM Serial Manager    ##################
#############################################################

class DSM:
    def __init__(self):
        '''
        @brief  Initializes serial manager 
        @param  None
        @retval None 
        '''
        self.hSerial = serial.Serial(C_SERIAL_COM_PORT, C_SERIAL_BAUD_RATE, timeout = C_SERIAL_TIMEOUT)

    def deinit(self):
        '''
        @brief  Deinitializes serial manager - closes serial port
        @param  None
        @retval None 
        '''
        self.hSerial.close()

    def write(self, data):
        '''
        @brief  Write data to serial port
        @param  data - input byte array
        @retval None 
        '''
        self.hSerial.write(data)

    def writeString(self, dataStr):
        '''
        @brief  Write string to serial port
        @param  data - input string 
        @retval None 
        '''
        byteArray = bytearray()
        byteArray.extend(map(ord, dataStr))
        self.write(byteArray)

    def readUntil(self, expected):
        '''
        @brief  Reads serial data until expected character
        @param  expected - expected end character
        @retval read string
        '''
        return self.hSerial.read_until(expected = expected)

    def readLine(self):
        '''
        @brief  Reads one line of serial data 
        @param  None
        @retval read string
        '''
        return self.hSerial.read_until()

    def getSerialPort(self):
        '''
        @brief  Returns serial port 
        @param  None
        @retval Serial port name 
        '''
        return self.hSerial.name

