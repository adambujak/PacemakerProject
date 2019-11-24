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
        self.dataRead = []
        self.unpackedDataRead = []

    def sendParams(self):
        # < indicates little endian, B indicates unsigned uint8, H indicates unsigned uint16
        paramsPackHeader = '<5B2H2B5H2B'
        paramsPack = pack(paramsPackHeader, 0x16, 0x55, 4, 50, 120, 3500, 3500, 10, 10, 2640, 2640, 250, 320, 150, 0,
                          8)
        self.ser.write(paramsPack)
        print("Sent Params: ", paramsPack)
        time.sleep(1)

    def sendEcho(self):
        # x indicates padding bytes which are necessary because the model is looking to read 23 bytes
        echoPackHeader = '<2B21x'
        echoPack = pack(echoPackHeader, 0x16, 0x22)
        self.ser.write(echoPack)
        print("Echo Out: ", echoPack)
        time.sleep(1)

    def readParams(self):
        print("In_buffer Before: ", self.ser.in_waiting)
        time.sleep(1)
        while self.ser.in_waiting < 21:
            print("Waiting for buffer to fill")
        print("Reading data...")
        self.dataRead = self.ser.read(self.ser.in_waiting)
        time.sleep(1)
        print("Data read...")
        time.sleep(1)
        print("In_buffer After: ", self.ser.in_waiting)
        time.sleep(1)
        print("Echo In: ", self.dataRead)

    def unpackParams(self):
        echoUnpackHeader = '<3B2H2B5H2B'
        self.unpackedDataRead = unpack(echoUnpackHeader, self.dataRead)
        print(self.unpackedDataRead)

    def closePort(self):
        self.ser.close()


def main():
    serComms = SerialManager()
    #serComms.sendParams()
    serComms.sendEcho()
    serComms.readParams()
    serComms.unpackParams()
    serComms.closePort()


main()
