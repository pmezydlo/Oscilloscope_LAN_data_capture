#!/usr/bin/env python

from telnetlib_receive_all import Telnet
from oscilloscope_functions import *
import sys
import time
import os
import numpy
import matplotlib.pyplot as plot
import psycopg2

port = 5555
osc_ip = "192.168.20.15"

try:

    ret = os.system("ping -c 1 " + osc_ip + " > /dev/null")

    if ret != 0:
        print "No response ping " + osc_ip
        sys.exit("ERROR")

    tn = Telnet(osc_ip, port);
    id = command(tn, "*IDN?")

    con = psycopg2.connect(database='measurement', user='pmezydlo')

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

    for x in range(100):
        for channel in chan: 
            vpp = 32.1#float(command(tn, ":" + channel +":VPP?"))
            vmax = 23.2#float(command(tn, ":" + channel +":VMAX?"))
            vmin = 0.5#float(command(tn, ":" + channel +":VMIN?"))

            cur = con.cursor()
            query = "INSERT INTO measurements VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, DEFAULT, %s, %s, %s, %s)"
            data = (ids[0],  ids[1],  ids[2], ids[3], osc_ip, port, channel, vpp, vmax, vmin)
            cur.execute(query, data)
            con.commit()
        time.sleep(0.2)

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:

    if con:
        con.close()
