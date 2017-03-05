from oscilloscope_functions import oscilloscope


lan_port = 5555
lan_osc_ip = "192.168.20.15"

usb_osc_path = "/dev/usbtmc1"

rs232_osc_path = "/dev/ttyUSB0"
rs232_osc_baudrate = 38400
rs232_osc_timeout = 1

#osc = oscilloscope(4, "lan", lan_osc_ip, lan_port)
osc = oscilloscope(4, "usb", usb_osc_path)

print('Manufacturer: {}'.format(osc.manufacturer))
print('Device: {}'.format(osc.dev_name))
print('Serial number: {}'.format(osc.serial_number))
print('Firmware version: {}'.format(osc.firmware_version))

osc.get_active_channel()

osc.plot("plot", ".png")

del osc
