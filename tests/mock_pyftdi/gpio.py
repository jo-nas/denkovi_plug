class Ftdi(object):
    def find_all(self, vps):
        devices = set()
        for vp in vps:
            if vp == (0x0403, 0x6001):
                devices.add((1027, 24577, u'test_serial', 1, u'discription'))
        return list(devices)


class GpioController(object):
    def __init__(self):
        self.opened = False
        self.output = None

    def open(self, vendor, product, interface, direction):
        self.opened = True

    @property
    def is_connected(self):
        return self.opened

    def read_port(self):
        return self.output

    def write_port(self, value):
        self.output = value

    def close(self):
        pass
