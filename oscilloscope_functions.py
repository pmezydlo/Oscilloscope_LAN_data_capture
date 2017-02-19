import sys
from measure_interfaces import device

class oscilloscope(device):
    def __init__ (self, *argv):
        argd = argv[1:]
        device.__init__(self, *argd)
        self.channel = argv[0]
        self.active_chan = []

    def __exit__ (self, *err):
        print "destructor"
        device.close()

    def get_active_channel(self):  
        chan = ["CHAN%d" % x for x in range(1, self.channel+1)]

        for check_chan in chan:
            ret = device.read(self, ":" + check_chan + ":DISP?") 
            if ret == '1\n':
                self.active_chan += [check_chan]
                print check_chan + " is active"

    def get_time(self):
        pass

    def plot(self, file_name ,file_type):
        time_scale = float(device.read(":TIM:SCAL?"))
        time_offset = float(device.read(":TIM:OFFS?"))

        print "Time scale: %.4f time offset: %.8fms" % (time_scale, time_offset)

        for channel in self.active_chan: 
            volt_scale = float(device.read(":" + channel + ":SCAL?"))
            volt_offset = float(device.read(":" + channel + ":OFFS?"))

            print channel + " offset value: %.4f scale value: %.4f" % (volt_offset, volt_scale)

            device.write(tn, ":WAV:POIN:MODE RAW")
            rawdata = device.read(":WAV:DATA? " + channel)[10:]
            device.write(":KEY:FORCE")

            size = len(rawdata)

            print "Data size: %d" % size

            data = numpy.frombuffer(rawdata, 'B')
            data = data + 255
            data = (data - 130.0 - volt_offset / volt_scale * 25) / 25 * volt_scale
            print data
            time = numpy.linspace(time_offset - 6 * time_scale, time_offset + 6 * time_scale, num = len(data))

            if time[-1] < 1e-3:
                time = time * 1e6
                tUnit = "uS"
            elif time[-1] < 1:
                time = time * 1e3
                tUnit = "mS"
            else:
                tUnit = "S"

            plot.plot(time, data)
            plot.title("Oscilloscope " + channel)
            plot.ylabel("Voltage (V)")
            plot.xlabel("Time ["+tUnit+"]")
            plot.xlim(time[0], time[-1])
        plot.savefig(file_name+'.png')
        
class multimeter(device):
    def __init__ (self, argv):
        pass

    def __del__ (self):
        pass

