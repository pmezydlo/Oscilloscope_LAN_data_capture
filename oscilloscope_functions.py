import sys
from telnetlib_receive_all import Telnet
import os

class usb:
    def __init__(self, dev_path):
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

class lan:
    def __init__(self, dev_ip, dev_port):
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

class device:
    def __init__ (self, *argv): 
        arg_len = len(argv)
        self.con_type = ""

        if arg_len == 1:
            self.con_type = "usb"
            self.dev_path = argv[0]
            self.dev = usb(self.dev_path)
        elif arg_len == 2:
            self.con_type = "lan"
            self.dev_ip = argv[0]
            self.dev_port = argv[1]
            self.dev = lan(self.dev_ip, self.dev_port)
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
