import serial
from struct import *
import time


class SerialManager:
    def __init__(self):
        self.port = 'COM10'
        self.baud = 115200
        self.timeout = 5
        self.ser = serial.Serial(self.port, self.baud, self.timeout)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.flush()
        self.paramsRead = []
        self.unpackedParamsRead = []
        self.egramRead = []
        self.unpackedEgramRead = []

    def sendParams(self):
        # < indicates little endian, B indicates unsigned uint8, H indicates unsigned uint16
        paramsPackHeader = '<5B2H2B5H2B'
        paramsPack = pack(paramsPackHeader, 0x16, 0x55, 1, 60, 120, 3500, 3500, 10, 10, 2640, 2640, 250, 320, 150, 0,
                          8)
        self.ser.write(paramsPack)
        print("Sent Params: ", paramsPack)
        time.sleep(1)

    def echoParams(self):
        # x indicates padding bytes which are necessary because the model is looking to read 23 bytes
        echoPackHeader = '<2B21x'
        echoPack = pack(echoPackHeader, 0x16, 0x22)
        self.ser.write(echoPack)
        time.sleep(.1)

    def readParams(self):
        # Expecting the received data to be 21 bytes
        while self.ser.in_waiting < 21:
            print("Waiting for buffer to fill")
        self.paramsRead = self.ser.read(self.ser.in_waiting)

    def unpackParams(self):
        # Specifying the format of the data received
        echoUnpackHeader = '<3B2H2B5H2B'
        self.unpackedParamsRead = unpack(echoUnpackHeader, self.paramsRead)

    def echoEgram(self):
        echoPackHeader = '<2B21x'
        echoPack = pack(echoPackHeader, 0x16, 0x47)
        self.ser.write(echoPack)

    def readEgram(self):
        while self.ser.in_waiting < 21:
            print("Waiting for buffer to fill")
        self.egramRead = self.ser.read(self.ser.in_waiting)

    def echoStopEgram(self):
        echoPackHeader = '<2B21x'
        echoPack = pack(echoPackHeader, 0x16, 0x62)
        self.ser.write(echoPack)
        time.sleep(1)

    def unpackEgram(self):
        echoUnpackHeader = '<2d5x'
        print(self.egramRead)
        self.unpackedEgramRead.append(unpack(echoUnpackHeader, self.egramRead))

    def closePort(self):
        self.ser.close()


def main():
    serComms = SerialManager()
    serComms.sendParams()
    serComms.echoParams()
    serComms.readParams()
    serComms.unpackParams()
    while serComms.unpackedParamsRead[2] == 0:
        serComms.echoParams()
        serComms.readParams()
        serComms.unpackParams()
    print("Received Data: ", serComms.unpackedParamsRead)
    '''serComms.sendParams()
    serComms.echoEgram()
    count = 0
    while count < 20:
        serComms.readEgram()
        serComms.unpackEgram()
        count += 1
        time.sleep(.1)
    serComms.echoStopEgram()
    print("Received Data: ", serComms.unpackedEgramRead)'''
    serComms.closePort()


main()
