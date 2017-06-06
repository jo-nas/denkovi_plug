import sys
import pytest
import mock_pyftdi

sys.modules['pyftdi'] = mock_pyftdi

import denkovi_plug


@pytest.fixture
def base_relay():
    return denkovi_plug.BaseRelayPlug(ident_code='test_serial')


# Test init
def test_it_raise_a_DeviceNotFoundException_if_device_cant_be_found():
    with pytest.raises(denkovi_plug.DeviceNotFoundException):
        denkovi_plug.BaseRelayPlug(ident_code='not_right')


def test_it_can_connect_if_ident_code_is_right(base_relay):
    assert isinstance(base_relay.connection, mock_pyftdi.gpio.GpioController)
    assert base_relay.connection.is_connected


def test_it_sets_the_outputs_to_off_on_startup(base_relay):
    assert base_relay.output == 0


# Test tearDown
def test_it_can_teardown_itself(base_relay):
    base_relay.tearDown()
    assert base_relay.connection is None


def test_it_turns_all_outputs_off_on_teardown(base_relay):
    base_relay.output = 255
    base_relay.tearDown()
    assert base_relay.output == 0


# Test open
def test_it_can_reopen_a_closed_connection(base_relay):
    base_relay.tearDown()
    base_relay.open()
    assert isinstance(base_relay.connection, mock_pyftdi.gpio.GpioController)
    assert base_relay.connection.is_connected


# Test output
def test_it_can_set_the_output(base_relay):
    for i in range(0, 255):
        base_relay.output = i
        assert base_relay.connection.read_port() == i


def test_it_has_the_same_cache_value_for_the_output(base_relay):
    for i in range(0, 255):
        base_relay.output = i
        assert base_relay._output == i


def test_it_has_the_right_output_value(base_relay):
    for i in range(0, 255):
        base_relay.output = i
        assert base_relay.output == i


# Test set
def test_it_can_set_a_given_pin_to_1(base_relay):
    for pin in range(1, 9):
        base_relay.set(pin, True)
        assert base_relay.output == 1 << (pin-1)
        base_relay.output = 0x00


def test_it_can_set_a_given_pin_to_0(base_relay):
    for pin in range(1, 9):
        base_relay.output = 0xFF
        base_relay.set(pin, False)
        assert base_relay.output == 0xFF & ~(1 << (pin-1))


def test_it_raise_a_InvalidPinExeception_if_the_given_pin_is_not_valid_on_set(base_relay):
    for address in range(-255, 255):
        if address not in range(1, 9):
            with pytest.raises(denkovi_plug.InvalidPinException):
                base_relay.set(address, True)


# Test get
def test_it_can_get_a_given_pin(base_relay):
    for pin in range(1, 9):
        base_relay.output = (1 << (pin-1))
        assert base_relay.get(pin) == 1
        base_relay.output = 0
        assert base_relay.get(pin) == 0


def test_it_raise_a_InvalidPinExeception_if_the_given_pin_is_not_valid_on_get(base_relay):
    for address in range(-255, 255):
        if address not in range(1, 9):
            with pytest.raises(denkovi_plug.InvalidPinException):
                base_relay.set(address, True)


# Test find_device
@pytest.fixture
def device():
    return denkovi_plug.BaseRelayPlug.find_device('test_serial')


def test_it_find_a_device(device):
    assert device is not None


def test_it_returns_a_serial_number(device):
    assert device["serial_number"] is not None


def test_it_returns_a_vendor_id(device):
    assert device["vendor"] is not None


def test_it_returns_a_product_id(device):
    assert device["product"] is not None


def test_it_returns_a_ifcount(device):
    assert device["ifcount"] is not None


def test_it_returns_a_description(device):
    assert device["description"] is not None


def test_it_returns_the_right_serial_number(device):
    assert device["serial_number"] == 'test_serial'


def test_it_returns_the_right_vendor_id(device):
    assert device["vendor"] == 0x0403


def test_it_returns_the_right_product_id(device):
    assert device["product"] == 0x6001


def test_it_returns_the_right_ifcount(device):
    assert device["ifcount"] == 1


def test_it_returns_the_right_description(device):
    assert device["description"] == "discription"


def test_it_returns_a_DeviceNotFoundException_if_device_is_not_found():
    with pytest.raises(denkovi_plug.DeviceNotFoundException):
        denkovi_plug.BaseRelayPlug.find_device('not_right')
