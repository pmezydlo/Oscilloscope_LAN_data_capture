import sys
from telnetlib_receive_all import Telnet
import os
import serial

class rs232:
    def __init__(self, dev_port, dev_baudrate, dev_timeout):
        print "rs232 init"
        try:
            self.serial = serial.Serial(dev_port, baudrate=dev_baudrate, timeout=dev_timeout)
        
            if not self.serial.isOpen():
                print "serial is not open"
                sys.exit("ERROR")
   
        except serial.SerialException:
            print "port already open"
            sys.exit("ERROR")

    def write(self, command):
        self.serial.write(command)

    def wread(self, command):
        self.serial.write(command)
        response = self.serial.readline()
        return response

    def close(self):
        self.serial.close()

class usb:
    def __init__(self, dev_path):
        print "usb init"
        self.device = dev_path
        self.FILE = os.open(dev_path, os.O_RDWR)

    def write(self, command):
        os.write(self.FILE, command)

    def read(self, command):
        response = ""
        r_char = ""
        self.write(command)

        while r_char != "\n":
            r_char = os.read(self.FILE, 1)
            response = response + r_char
        return response

    def close(self):
        self.FILE.close()

class lan:
    def __init__(self, dev_ip, dev_port):
        print "lan init"
        self.dev_port = dev_port
        self.dev_ip = dev_ip
        self.tn = Telnet(dev_ip, dev_port) 

    def read(self, command):
        wait = 1
        response = ""
        while response != "1\n":
            self.tn.write("*OPC?\n")
            response = self.tn.read_until("\n", wait)

        self.tn.write(command + "\n")
        return self.tn.read_until("\n", wait)

    def write(self, command):
        self.tn.write(command + "\n")

    def ping(self):
        return os.system("ping -c 1 " + osc_ip + " > /dev/null")

    def close(self):
        self.tn.close()

class device:
    def __init__ (self, *argv): 
        arg_len = len(argv)
        self.con_type = argv[0]

        if self.con_type == "usb":
            if arg_len == 2:
                self.dev_path = argv[1]
                self.dev = usb(self.dev_path)
            else:
                print "bad arg list"
                sys.exit("ERROR")

        elif self.con_type == "lan":
            if arg_len == 3:
                self.dev_ip = argv[1]
                self.dev_port = argv[2]
                self.dev = lan(self.dev_ip, self.dev_port)
            else:
                print "bad arg list"
                sys.exit("ERROR")
        elif self.con_type == "rs232":
            if arg_len == 4:
                self.dev_port = argv[1]
                self.dev_baudrate = argv[2]
                self.dev_timeout = argv[3]
                self.dev = rs232(self.dev_port, self.dev_baudrate, self.dev_timeout)
            else:
                print "bad arg list"
                sys.exit("ERROR");
        else:
            print "bad arg list"
    
        id = self.dev.read("*IDN?")
        
        if id == "command_error":
            print "No response from device"
            sys.exit("ERROR")

        ids = id.split(',')

        self.manufacturer = ids[0]
        self.dev_name = ids[1]
        self.serial_number = ids[2]
        self.firmware_version = ids[3]

    def write(self, command):
        return self.dev.write(command)

    def read(self, command):
        self.dev.read(command)

    def close(self):
        self.dev.close()

class oscilloscope(device):
    def __init__ (self):
        pass
