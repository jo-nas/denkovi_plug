# Denkovi Relais Plug
[![Build Status](https://travis-ci.org/jo-nas/denkovi_plug.svg?branch=master)](https://travis-ci.org/jo-nas/denkovi_plug) [![Coverage Status](https://coveralls.io/repos/github/jo-nas/denkovi_plug/badge.svg?branch=master)](https://coveralls.io/github/jo-nas/denkovi_plug?branch=master)  
A package for openhtf plugs to control the denkovi relay boards.

## Installation
To install the plug you can use PIP:
```bash
pip install git+https://github.com/jo-nas/denkovi_plug.git
```

## Usage
4 Channel Relay Board:
```python
import openhtf
from denkovi_plug.four_relais import FourRelais
  
@openhtf.plug(relais=FourRelais)
def test_phase(test, relais):
    relais.channel_1 = True
    relais.channel_2 = True
    relais.channel_3 = True
    relais.channel_4 = True
    relais.all = False
    
    if relais.channel_1 is False:
        print("Relay 1 is off")
```

8 Channel Relay Board:
```python
import openhtf
from denkovi_plug.eight_relais import EightRelais
  
@openhtf.plug(relais=EightRelais)
def test_phase(test, relais):
    relais.channel_1 = True
    relais.channel_2 = True
    relais.channel_3 = True
    relais.channel_4 = True
    relais.channel_5 = True
    relais.channel_6 = True
    relais.channel_7 = True
    relais.channel_8 = True
    relais.all = False
    
    if relais.channel_1 is False:
        print("Relay 1 is off")
```

16 Channel Relay Board:
```python
import openhtf
from denkovi_plug.eight_relais import SixTeenChannelBoard
  
@openhtf.plug(relais=SixTeenChannelBoard)
def test_phase(test, relais):
    relais.channel_1 = True
    relais.channel_2 = True
    relais.channel_3 = True
    relais.channel_4 = True
    relais.channel_5 = True
    relais.channel_6 = True
    relais.channel_7 = True
    relais.channel_8 = True
    relais.channel_9 = True
    relais.channel_10 = True
    relais.channel_11 = True
    relais.channel_12 = True
    relais.channel_13 = True
    relais.channel_14 = True
    relais.channel_15 = True
    relais.channel_16 = True
    relais.all = False
    
    if relais.channel_1 is False:
        print("Relay 1 is off")
```
## Requirements
- [openhtf](https://github.com/google/openhtf): The open-source hardware testing framework.
- [pyftdi V0.13.4](https://github.com/eblot/pyftdi): FTDI device driver written in pure Python.
- [pyserial V3.3](https://github.com/pyserial/pyserial): Python serial port access library.

## Authors
*denkovi_plug* was written by *Jonas Steinkamp <jonas@steinka.mp>*.
