from openhtf import conf

class DeviceNotFoundException(Exception):
    pass


class InvalidPinException(Exception):
    pass


ALL_OFF = 0b00000000
ALL_ON = 0b11111111
ALL_FTDI_IDS = tuple((0x0403, p) for p in (0x6001, 0x6010, 0x6011, 0x6014))


class BaseRelayPlug(object):
    @conf.inject_positional_args
    def __init__(self, ident_code):
        self._output = None
        self.ident_code = ident_code
        self.open_called = 0
        self.tearDown_called = 0

        self.open()
        self.output = ALL_OFF

    def tearDown(self):
        self.tearDown_called += 1

    def open(self):
        self.open_called += 1

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, bit_mask):
        self._output = bit_mask

    def set(self, pin, on):
        if on:
            self.output = self._output | (1 << (pin-1))
        else:
            self.output = self._output & ~ (1 << (pin-1))

    def get(self, pin):
        return bool(self.output & (1 << (pin-1)))

    @staticmethod
    def find_device(ident_code):
        return {
            'serial_number': u'test_serial',
            'product': 0x6001,
            'vendor': 0x0403,
            'ifcount': 1,
            'description': u'discription'
        }
