# -*- coding: utf-8 -*-
from pyftdi import gpio
from openhtf import conf
from openhtf import plugs

__author__ = 'Jonas Steinkamp'
__email__ = 'jonas@steinka.mp'
__version__ = '0.1.0'

ALL_OFF = 0b00000000
ALL_ON = 0b11111111
ALL_FTDI_IDS = tuple((0x0403, p) for p in (0x6001, 0x6010, 0x6011, 0x6014))


class DeviceNotFoundException(Exception):
    pass


class InvalidPinException(Exception):
    pass

conf.declare('ident_code', description='The name of the Device.')


class BaseRelayPlug(plugs.BasePlug):
    @conf.inject_positional_args
    def __init__(self, ident_code):
        self._output = None
        self.connection = gpio.GpioController()
        self.ident_code = ident_code

        self.open()
        self.output = ALL_OFF

    def tearDown(self):
        self.output = ALL_OFF
        self.connection.close()
        self.connection = None

    def open(self):
        if self.connection is None:
            self.connection = gpio.GpioController()
        device = self.find_device(self.ident_code)
        self.connection.open(device["vendor"], device["product"], interface=0, direction=255)

    @property
    def output(self):
        if self.connection:
            self._output = self.connection.read_port()
        return self._output

    @output.setter
    def output(self, bit_mask):
        self._output = bit_mask
        self.connection.write_port(self._output)

    def set(self, pin, on):
        if pin > 8 or 0 >= pin:
            raise InvalidPinException("The pin {} is not a valid pin. Only 1-8 are valid".format(pin))
        if on:
            self.output = self._output | (1 << (pin-1))
        else:
            self.output = self._output & ~ (1 << (pin-1))

    def get(self, pin):
        return bool(self.output & (1 << (pin-1)))

    @staticmethod
    def find_device(ident_code):
        devices = gpio.Ftdi().find_all(ALL_FTDI_IDS)
        for device in devices:
            if ident_code in device:
                dict_desc = ('vendor', 'product', 'serial_number', 'ifcount', 'description')
                return dict(zip(dict_desc, device))
        else:
            raise DeviceNotFoundException("Device '{}' can't be found.".format(ident_code))
