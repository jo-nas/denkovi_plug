import pytest
import mock_serial
import sys
sys.modules["serial"] = mock_serial
import denkovi_plug


@pytest.fixture
def relay():
    from denkovi_plug import relay_boards
    return relay_boards.SixTeenChannelBoard()


def test_it_activates_channel_1(relay):
    relay.channel_1 = True
    assert relay._output == 0b1000000000000000


def test_it_activates_channel_2(relay):
    relay.channel_2 = True
    assert relay._output == 0b0100000000000000


def test_it_activates_channel_3(relay):
    relay.channel_3 = True
    assert relay._output == 0b0010000000000000


def test_it_activates_channel_4(relay):
    relay.channel_4 = True
    assert relay._output == 0b0001000000000000


def test_it_activates_channel_5(relay):
    relay.channel_5 = True
    assert relay._output == 0b0000100000000000


def test_it_activates_channel_6(relay):
    relay.channel_6 = True
    assert relay._output == 0b0000010000000000


def test_it_activates_channel_7(relay):
    relay.channel_7 = True
    assert relay._output == 0b0000001000000000


def test_it_activates_channel_8(relay):
    relay.channel_8 = True
    assert relay._output == 0b0000000100000000


def test_it_activates_channel_9(relay):
    relay.channel_9 = True
    assert relay._output == 0b0000000010000000


def test_it_activates_channel_10(relay):
    relay.channel_10 = True
    assert relay._output == 0b0000000001000000


def test_it_activates_channel_11(relay):
    relay.channel_11 = True
    assert relay._output == 0b0000000000100000


def test_it_activates_channel_12(relay):
    relay.channel_12 = True
    assert relay._output == 0b0000000000010000


def test_it_activates_channel_13(relay):
    relay.channel_13 = True
    assert relay._output == 0b0000000000001000


def test_it_activates_channel_14(relay):
    relay.channel_14 = True
    assert relay._output == 0b0000000000000100


def test_it_activates_channel_15(relay):
    relay.channel_15 = True
    assert relay._output == 0b0000000000000010


def test_it_activates_channel_16(relay):
    relay.channel_16 = True
    assert relay._output == 0b0000000000000001

def test_it_activates_all_channels(relay):
    relay.all = True
    assert relay._output == 0b1111111111111111


def test_it_deactivates_channel_1(relay):
    relay._output = 0b1111111111111111
    relay.channel_1 = False
    assert relay._output == 0b0111111111111111


def test_it_deactivates_channel_2(relay):
    relay._output = 0b1111111111111111
    relay.channel_2 = False
    assert relay._output == 0b1011111111111111


def test_it_deactivates_channel_3(relay):
    relay._output = 0b1111111111111111
    relay.channel_3 = False
    assert relay._output == 0b1101111111111111


def test_it_deactivates_channel_4(relay):
    relay._output = 0b1111111111111111
    relay.channel_4 = False
    assert relay._output == 0b1110111111111111


def test_it_deactivates_channel_5(relay):
    relay._output = 0b1111111111111111
    relay.channel_5 = False
    assert relay._output == 0b1111011111111111


def test_it_deactivates_channel_6(relay):
    relay._output = 0b1111111111111111
    relay.channel_6 = False
    assert relay._output == 0b1111101111111111


def test_it_deactivates_channel_7(relay):
    relay._output = 0b1111111111111111
    relay.channel_7 = False
    assert relay._output == 0b1111110111111111


def test_it_deactivates_channel_8(relay):
    relay._output = 0b1111111111111111
    relay.channel_8 = False
    assert relay._output == 0b1111111011111111


def test_it_deactivates_channel_9(relay):
    relay._output = 0b1111111111111111
    relay.channel_9 = False
    assert relay._output == 0b1111111101111111


def test_it_deactivates_channel_10(relay):
    relay._output = 0b1111111111111111
    relay.channel_10 = False
    assert relay._output == 0b1111111110111111


def test_it_deactivates_channel_11(relay):
    relay._output = 0b1111111111111111
    relay.channel_11 = False
    assert relay._output == 0b1111111111011111


def test_it_deactivates_channel_12(relay):
    relay._output = 0b1111111111111111
    relay.channel_12 = False
    assert relay._output == 0b1111111111101111


def test_it_deactivates_channel_13(relay):
    relay._output = 0b1111111111111111
    relay.channel_13 = False
    assert relay._output == 0b1111111111110111


def test_it_deactivates_channel_14(relay):
    relay._output = 0b1111111111111111
    relay.channel_14 = False
    assert relay._output == 0b1111111111111011


def test_it_deactivates_channel_15(relay):
    relay._output = 0b1111111111111111
    relay.channel_15 = False
    assert relay._output == 0b1111111111111101


def test_it_deactivates_channel_16(relay):
    relay._output = 0b1111111111111111
    relay.channel_16 = False
    assert relay._output == 0b1111111111111110

def test_it_deactivates_all_channels(relay):
    relay._output = 0b1111111111111111
    relay.all = False
    assert relay._output == 0b0000000000000000


def test_it_can_get_true_from_channel_1(relay):
    relay._output = 0b1000000000000000
    assert relay.channel_1 is True


def test_it_can_get_false_from_channel_1(relay):
    relay._output = 0b0111111111111111
    assert relay.channel_1 is False


def test_it_can_get_true_from_channel_2(relay):
    relay._output = 0b0100000000000000
    assert relay.channel_2 is True


def test_it_can_get_false_from_channel_2(relay):
    relay._output = 0b1011111111111111
    assert relay.channel_2 is False


def test_it_can_get_true_from_channel_3(relay):
    relay._output = 0b0010000000000000
    assert relay.channel_3 is True


def test_it_can_get_false_from_channel_3(relay):
    relay._output = 0b1101111111111111
    assert relay.channel_3 is False


def test_it_can_get_true_from_channel_4(relay):
    relay._output = 0b0001000000000000
    assert relay.channel_4 is True


def test_it_can_get_false_from_channel_4(relay):
    relay._output = 0b1110111111111111
    assert relay.channel_4 is False


def test_it_can_get_true_from_channel_5(relay):
    relay._output = 0b0000100000000000
    assert relay.channel_5 is True


def test_it_can_get_false_from_channel_5(relay):
    relay._output = 0b1111011111111111
    assert relay.channel_5 is False


def test_it_can_get_true_from_channel_6(relay):
    relay._output = 0b0000010000000000
    assert relay.channel_6 is True


def test_it_can_get_false_from_channel_6(relay):
    relay._output = 0b1111101111111111
    assert relay.channel_6 is False


def test_it_can_get_true_from_channel_7(relay):
    relay._output = 0b0000001000000000
    assert relay.channel_7 is True


def test_it_can_get_false_from_channel_7(relay):
    relay._output = 0b1111110111111111
    assert relay.channel_7 is False


def test_it_can_get_true_from_channel_8(relay):
    relay._output = 0b0000000100000000
    assert relay.channel_8 is True


def test_it_can_get_false_from_channel_8(relay):
    relay._output = 0b1111111011111111
    assert relay.channel_8 is False


def test_it_can_get_true_from_channel_9(relay):
    relay._output = 0b0000000010000000
    assert relay.channel_9 is True


def test_it_can_get_false_from_channel_9(relay):
    relay._output = 0b1111111101111111
    assert relay.channel_9 is False


def test_it_can_get_true_from_channel_10(relay):
    relay._output = 0b0000000001000000
    assert relay.channel_10 is True


def test_it_can_get_false_from_channel_10(relay):
    relay._output = 0b1111111110111111
    assert relay.channel_10 is False


def test_it_can_get_true_from_channel_11(relay):
    relay._output = 0b0000000000100000
    assert relay.channel_11 is True


def test_it_can_get_false_from_channel_11(relay):
    relay._output = 0b1111111111011111
    assert relay.channel_11 is False


def test_it_can_get_true_from_channel_12(relay):
    relay._output = 0b0000000000010000
    assert relay.channel_12 is True


def test_it_can_get_false_from_channel_12(relay):
    relay._output = 0b1111111111101111
    assert relay.channel_12 is False


def test_it_can_get_true_from_channel_13(relay):
    relay._output = 0b0000000000001000
    assert relay.channel_13 is True


def test_it_can_get_false_from_channel_13(relay):
    relay._output = 0b1111111111110111
    assert relay.channel_13 is False


def test_it_can_get_true_from_channel_14(relay):
    relay._output = 0b0000000000000100
    assert relay.channel_14 is True


def test_it_can_get_false_from_channel_14(relay):
    relay._output = 0b1111111111111011
    assert relay.channel_14 is False


def test_it_can_get_true_from_channel_15(relay):
    relay._output = 0b0000000000000010
    assert relay.channel_15 is True


def test_it_can_get_false_from_channel_15(relay):
    relay._output = 0b1111111111111101
    assert relay.channel_15 is False


def test_it_can_get_true_from_channel_16(relay):
    relay._output = 0b0000000000000001
    assert relay.channel_16 is True


def test_it_can_get_false_from_channel_16(relay):
    relay._output = 0b1111111111111110
    assert relay.channel_16 is False


def test_it_can_get_true_from_all_channels(relay):
    relay._output = 0b1111111111111111
    assert relay.all == 0b1111111111111111


def test_it_can_get_false_from_all_channels(relay):
    relay._output = 0b0000000000000000
    assert relay.all == 0b0000000000000000
