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

    con = psycopg2.connect(database='osci_meas', user='pmezydlo')

    if id == "command error":
        print "No response for Oscilloscope"
        sys.exit("ERROR")

    ids = id.split(',')
    print "Manufacturer: " + ids[0]
    print "Device: " + ids[1]
    print "Serial number: " + ids[2]
    print "Firmware version: " + ids[3]

    cur = con.cursor()
    query = "INSERT INTO device VALUES(DEFAULT, %s, %s, %s, %s, %s, %s)"
    data = (ids[0],  ids[1],  ids[2], ids[3], osc_ip, port)
    cur.execute(query, data)
    con.commit()

    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:

    if con:
        con.close()
