from oscilloscope_functions import *


port = 5555
osc_ip = "192.168.20.15"
osc_path = "/dev/usbtmc1"

osc = device(osc_ip, port)
#osc = device("/dev/usbtmc1")



print "Manufacturer: ", osc.manufacturer
print "Device: " + osc.dev_name
print "Serial number: ", osc.serial_number
print "Firmware version: ", osc.firmware_version


