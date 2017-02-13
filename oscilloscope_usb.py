from oscilloscope_functions import *


lan_port = 5555
lan_osc_ip = "192.168.20.15"

usb_osc_path = "/dev/usbtmc1"

rs232_osc_path = "/dev/ttyUSB0"
rs232_osc_baudrate = 38400
rs232_osc_timeout = 1

#osc = device("usb", usb_osc_path)
osc = device("lan", lan_osc_ip, lan_port)
#sc = device("rs232", rs232_osc_path, rs232_osc_baudrate, rs232_osc_timeout)

print "Manufacturer: ", osc.manufacturer
print "Device: " + osc.dev_name
print "Serial number: ", osc.serial_number
print "Firmware version: ", osc.firmware_version

osc.close()
