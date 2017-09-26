# -*- coding: utf-8 -*-
import denkovi_plug
from openhtf import conf
import serial
from serial.tools import list_ports
import time
from struct import *

__author__ = 'Jonas Steinkamp'
__email__ = 'jonas@steinka.mp'


class FourChannelBoard(denkovi_plug.BaseRelayPlug):
    IDENTIFICATION_CODE = 'DAE002hw'

    @property
    def channel_1(self):
        return self.get(1)

    @channel_1.setter
    def channel_1(self, on):
        self.set(1, on)

    @property
    def channel_2(self):
        return self.get(2)

    @channel_2.setter
    def channel_2(self, on):
        self.set(2, on)

    @property
    def channel_3(self):
        return self.get(3)

    @channel_3.setter
    def channel_3(self, on):
        self.set(3, on)

    @property
    def channel_4(self):
        return self.get(4)

    @channel_4.setter
    def channel_4(self, on):
        self.set(4, on)

    @property
    def all(self):
        return self.output

    @all.setter
    def all(self, on):
        if on:
            self.output = 0xFF
        else:
            self.output = 0x00


class EightChannelBoard(FourChannelBoard):
    IDENTIFICATION_CODE = 'DAE002hw'

    @property
    def channel_5(self):
        return self.get(5)

    @channel_5.setter
    def channel_5(self, on):
        self.set(5, on)

    @property
    def channel_6(self):
        return self.get(6)

    @channel_6.setter
    def channel_6(self, on):
        self.set(6, on)

    @property
    def channel_7(self):
        return self.get(7)

    @channel_7.setter
    def channel_7(self, on):
        self.set(7, on)

    @property
    def channel_8(self):
        return self.get(8)

    @channel_8.setter
    def channel_8(self, on):
        self.set(8, on)


class SixTeenChannelBoard(EightChannelBoard):
    def __init__(self, ident_code='DAE002oH'):
        self._output = None
        self.connection = self.find_device(ident_code)
        self.all = False

    def tearDown(self):
        self.all = False
        self.connection.close()
        self.connection = None

    @property
    def output(self):
        if self.connection:
            self.connection.write("ask//")
            try:
                self._output = unpack(">H", self.connection.read(2))[0]
            except:
                pass
        return self._output

    @output.setter
    def output(self, bit_mask):
        self._output = bit_mask
        time.sleep(0.05)
        self.connection.flushInput()
        self.connection.flushOutput()
        self.connection.write("x{}//".format(pack('>H', self._output)))

    def set(self, pin, on):
        if on:
            self.output = self._output | (1 << (16-pin))
        else:
            self.output = self._output & ~(1 << (16-pin))

    def get(self, pin):
        return bool(self.output & (1 << (16-pin)))

    @staticmethod
    def find_device(ident_code):
        for e in list(list_ports.comports()):
            if e.serial_number == ident_code:
                device = serial.Serial(
                    port=e.device,
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    xonxoff=0,  # no software flow control
                    rtscts=0,  # no RTS/CTS flow control
                    timeout=1.0,
                    writeTimeout=1.0)
                return device
        raise denkovi_plug.DeviceNotFoundException("Device '{}' can't be found.".format(ident_code))

    @property
    def channel_9(self):
        return self.get(9)

    @channel_9.setter
    def channel_9(self, on):
        self.set(9, on)

    @property
    def channel_10(self):
        return self.get(10)

    @channel_10.setter
    def channel_10(self, on):
        self.set(10, on)

    @property
    def channel_11(self):
        return self.get(11)

    @channel_11.setter
    def channel_11(self, on):
        self.set(11, on)

    @property
    def channel_12(self):
        return self.get(12)

    @channel_12.setter
    def channel_12(self, on):
        self.set(12, on)

    @property
    def channel_13(self):
        return self.get(13)

    @channel_13.setter
    def channel_13(self, on):
        self.set(13, on)

    @property
    def channel_14(self):
        return self.get(14)

    @channel_14.setter
    def channel_14(self, on):
        self.set(14, on)

    @property
    def channel_15(self):
        return self.get(15)

    @channel_15.setter
    def channel_15(self, on):
        self.set(15, on)

    @property
    def channel_16(self):
        return self.get(16)

    @channel_16.setter
    def channel_16(self, on):
        self.set(16, on)

    @property
    def all(self):
        return self.output

    @all.setter
    def all(self, on):
        if on:
            self.output = 0xFFFF
        else:
            self.output = 0x00000

if __name__ == '__main__':
    relayboard = SixTeenChannelBoard()
    relayboard.channel_16 = True