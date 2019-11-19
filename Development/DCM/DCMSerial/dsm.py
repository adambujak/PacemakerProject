import serial



class DSM:
    def __init__(self):
        self.hSerial = serial.Serial(C_SERIAL_COM_PORT, C_SERIAL_BAUD_RATE, timeout = C_SERIAL_TIMEOUT)

    def deinit(self):
        self.hSerial.close()

    def write(self, data):
        self.hSerial.write(bdata)
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port