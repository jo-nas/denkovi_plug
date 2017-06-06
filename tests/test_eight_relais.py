import pytest
import mock_denkovi_plug

import denkovi_plug


@pytest.fixture
def relay():
    denkovi_plug.BaseRelayPlug = mock_denkovi_plug.BaseRelayPlug
    from denkovi_plug import relay_boards

    return relay_boards.EightChannelBoard()


def test_it_activates_channel_1(relay):
    relay.channel_1 = True
    assert relay._output == 0b00000001


def test_it_activates_channel_2(relay):
    relay.channel_2 = True
    assert relay._output == 0b00000010


def test_it_activates_channel_3(relay):
    relay.channel_3 = True
    assert relay._output == 0b00000100


def test_it_activates_channel_4(relay):
    relay.channel_4 = True
    assert relay._output == 0b00001000


def test_it_activates_channel_5(relay):
    relay.channel_5 = True
    assert relay._output == 0b00010000


def test_it_activates_channel_6(relay):
    relay.channel_6 = True
    assert relay._output == 0b00100000


def test_it_activates_channel_7(relay):
    relay.channel_7 = True
    assert relay._output == 0b01000000


def test_it_activates_channel_8(relay):
    relay.channel_8 = True
    assert relay._output == 0b10000000


def test_it_activates_all_channels(relay):
    relay.all = True
    assert relay._output == 0b11111111


def test_it_deactivates_channel_1(relay):
    relay._output = 0b11111111
    relay.channel_1 = False
    assert relay._output == 0b11111110


def test_it_deactivates_channel_2(relay):
    relay._output = 0b11111111
    relay.channel_2 = False
    assert relay._output == 0b11111101


def test_it_deactivates_channel_3(relay):
    relay._output = 0b11111111
    relay.channel_3 = False
    assert relay._output == 0b11111011


def test_it_deactivates_channel_4(relay):
    relay._output = 0b11111111
    relay.channel_4 = False
    assert relay._output == 0b11110111


def test_it_deactivates_channel_5(relay):
    relay._output = 0b11111111
    relay.channel_5 = False
    assert relay._output == 0b11101111


def test_it_deactivates_channel_6(relay):
    relay._output = 0b11111111
    relay.channel_6 = False
    assert relay._output == 0b11011111


def test_it_deactivates_channel_7(relay):
    relay._output = 0b11111111
    relay.channel_7 = False
    assert relay._output == 0b10111111


def test_it_deactivates_channel_8(relay):
    relay._output = 0b11111111
    relay.channel_8 = False
    assert relay._output == 0b01111111


def test_it_deactivates_all_channels(relay):
    relay._output = 0b11111111
    relay.all = False
    assert relay._output == 0b00000000
