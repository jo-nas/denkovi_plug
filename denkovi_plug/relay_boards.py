# -*- coding: utf-8 -*-
import denkovi_plug
from openhtf import conf

__author__ = 'Jonas Steinkamp'
__email__ = 'jonas@steinka.mp'


class FourChannelBoard(denkovi_plug.BaseRelayPlug):
    @conf.save_and_restore(ident_code='DAE002hw')
    def __init__(self):
        super(self.__class__, self).__init__()

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


class EightChannelBoard(denkovi_plug.BaseRelayPlug):
    @conf.save_and_restore(ident_code='DAE002hw')
    def __init__(self):
        super(self.__class__, self).__init__()

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

    @property
    def all(self):
        return self.output

    @all.setter
    def all(self, on):
        if on:
            self.output = 0xFF
        else:
            self.output = 0x00
