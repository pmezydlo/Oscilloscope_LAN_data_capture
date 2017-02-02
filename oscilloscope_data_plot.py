#!/usr/bin/env python

from telnetlib_receive_all import Telnet
from oscilloscope_functions import *
import sys
import time
import os
import numpy
import matplotlib.pyplot as plot

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

command(tn, ":STOP")

chan = []
for channel in ["CHAN1", "CHAN2", "CHAN3", "CHAN4", "MATH"]:
    ret = command(tn, ":" + channel + ":DISP?")

    if ret == '1\n':
        chan += [channel]
        print channel + " is active"

time_scale = float(command(tn, ":TIM:SCAL?"))
time_offset = float(command(tn, ":TIM:OFFS?"))

print "Time scale: %.4f time offset: %.8fms" % (time_scale, time_offset)

for channel in chan: 
    volt_scale = float(command(tn, ":" + channel + ":SCAL?"))
    volt_offset = float(command(tn, ":" + channel + ":OFFS?"))

    print channel + " offset value: %.4f scale value: %.4f" % (volt_offset, volt_scale)

    command(tn, ":WAV:POIN:MODE RAW")
    rawdata = command(tn, ":WAV:DATA? " + channel)[10:]
    command(tn, ":KEY:FORCE")

    size = len(rawdata)

    print "Data size: %d" % size

    data = numpy.frombuffer(rawdata, 'B')
    data = data + 255
    data = (data - 130.0 - volt_offset / volt_scale * 25) / 25 * volt_scale
    print data
    time = numpy.linspace(time_offset - 6 * time_scale, time_offset + 6 * time_scale, num = len(data))


#    if time[-1] < 1e-3:
#        time = time * 1e6
#        tUnit = "uS"
#    elif time[-1] < 1:
#        time = time * 1e3
#        tUnit = "mS"
#    else:
#        tUnit = "S"

    plot.plot(time, data)
    plot.title("Oscilloscope " + channel)
    plot.ylabel("Voltage (V)")
 #   plot.xlabel("Time ["+tUnit+"]")
    plot.xlim(time[0], time[-1])
    plot.savefig('plot_'+channel+'.png')