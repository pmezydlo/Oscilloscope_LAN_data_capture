from oscilloscope_functions import *


lan_port = 5555
lan_osc_ip = "192.168.20.15"

usb_osc_path = "/dev/usbtmc1"

rs232_osc_path = "/dev/ttyUSB0"
rs232_osc_baudrate = 38400
rs232_osc_timeout = 1

#osc = device("usb", usb_osc_path)
osc = oscilloscope(4, "lan", lan_osc_ip, lan_port)
#sc = device("rs232", rs232_osc_path, rs232_osc_baudrate, rs232_osc_timeout)

#osc = oscilloscope(channel=4, con_type="lan", lan_ip=lan_osc_ip, lan_port=lan_port)

print "Manufacturer: ", osc.manufacturer
print "Device: " + osc.dev_name
print "Serial number: ", osc.serial_number
print "Firmware version: ", osc.firmware_version

osc.get_active_channel()

osc.close()
