# Author: Adam Bujak
# Date Created: Monday, November 19, 2019
# Description: DCM Serial Manager
# Filename: dsm.py

import serial
from src.dcm_constants import *
from Common.failCodes  import *


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
        try:
            self.hSerial = serial.Serial(C_SERIAL_COM_PORT, C_SERIAL_BAUD_RATE, timeout = C_SERIAL_TIMEOUT)
        except:
            print("Error Opening Com Port")
            self.hSerial = None
        
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
        if (self.checkSerialPort() == FailureCodes.CANNOT_OPEN_COM_PORT):
            return FailureCodes.CANNOT_OPEN_COM_PORT
        print("Serial write data", data)
        print("Serial write data length", len(data))
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

    def read(self, size):
        '''
        @brief  Reads n bytes of serial data 
        @param  size - size of data in bytes
        @retval read string
        '''
        if (self.checkSerialPort() == FailureCodes.CANNOT_OPEN_COM_PORT):
            return FailureCodes.CANNOT_OPEN_COM_PORT
        return self.hSerial.read(size = size)

    def readUntil(self, expected):
        '''
        @brief  Reads serial data until expected character
        @param  expected - expected end character
        @retval read string
        '''
        if (self.checkSerialPort() == FailureCodes.CANNOT_OPEN_COM_PORT):
            return FailureCodes.CANNOT_OPEN_COM_PORT
        return self.hSerial.read_until(expected = expected)

    def readLine(self):
        '''
        @brief  Reads one line of serial data 
        @param  None
        @retval read string
        '''
        if (self.checkSerialPort() == FailureCodes.CANNOT_OPEN_COM_PORT):
            return FailureCodes.CANNOT_OPEN_COM_PORT
        return self.hSerial.read_until()

    def getSerialPort(self):
        '''
        @brief  Returns serial port 
        @param  None
        @retval Serial port name 
        '''
        if (self.checkSerialPort() == FailureCodes.CANNOT_OPEN_COM_PORT):
            return FailureCodes.CANNOT_OPEN_COM_PORT
        return self.hSerial.name

    def checkSerialPort(self):
        '''
        @brief  Checks to see if serial port is open and available 
        @param  None
        @retval True / FailuteCode.CANNOT_OPEN_COM_PORT
        '''
        if (self.hSerial == None):
            try:
                self.hSerial = serial.Serial(C_SERIAL_COM_PORT, C_SERIAL_BAUD_RATE, timeout = C_SERIAL_TIMEOUT)
            except:
                print("Error Opening Com Port")
                self.hSerial = None
                return FailureCodes.CANNOT_OPEN_COM_PORT
        return True