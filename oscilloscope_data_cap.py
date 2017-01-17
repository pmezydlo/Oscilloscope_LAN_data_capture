#!/usr/bin/env python

from telnetlib_receive_all import Telnet
import sys
import time
import os

port = 5555
osc_ip = "192.168.20.15"

response = os.system("ping -c 1 " + osc_ip + " > /dev/null")

if response != 0:
    print "No response ping " + osc_ip
    sys.exit("ERROR")

print "OK"
print "this is new commit"
