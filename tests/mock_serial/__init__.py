PARITY_NONE=0
STOPBITS_ONE=0
EIGHTBITS=0

class Serial:
    def __init__(self, port, baudrate, parity, stopbits, bytesize, xonxoff, rtscts, timeout, writeTimeout):
        self.write_data = ""
        pass

    def flushInput(self):
        pass

    def flushOutput(self):
        pass

    def write(self, data):
        self.write_data = data

    def read(self, length):
        return "\x00"*length*2

