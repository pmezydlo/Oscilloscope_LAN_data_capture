#!/usr/bin/env python

from telnetlib_receive_all import Telnet
from oscilloscope_functions import *
import sys
import time
import os

port = 5555
osc_ip = "192.168.20.15"

ret = os.system("ping -c 1 " + osc_ip + " > /dev/null")

if ret != 0:
    print "No response ping " + osc_ip
    sys.exit("ERROR")

tn = Telnet(osc_ip, port);
id = command(tn, "*IDN?")

if id == "command error":
    print "No response for Oscilloscope"
    sys.exit("ERROR")

ids = id.split(',')
print "Manufacturer: " + ids[0]
print "Device: " + ids[1]
print "Serial number: " + ids[2]
print "Firmware version: " + ids[3]

chan = []
for channel in ["CHAN1", "CHAN2", "CHAN3", "CHAN4", "MATH"]:
    ret = command(tn, ":" + channel + ":DISP?")

    if ret == '1\n':
        chan += [channel]
        print channel + " is active"
