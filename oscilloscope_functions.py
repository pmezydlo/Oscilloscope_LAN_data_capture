import sys
from measure_interfaces import device
import numpy
import matplotlib.pyplot as plot

class oscilloscope(device):
    def __init__(self, *argv):
        argd = argv[1:]
        device.__init__(self, *argd)
        self.channel = argv[0]
        self.active_chan = []

    def get_active_channel(self):  
        chan = ["CHAN%d" % x for x in range(1, self.channel+1)]

        for check_chan in chan:
            ret = device.read(self, ":" + check_chan + ":DISP?") 
            if ret == '1\n':
                self.active_chan += [check_chan]
                print('{} is active'.format(check_chan))

    def get_time(self):
        pass

    def plot(self, file_name ,file_type):
        time_scale = float(device.read(self, ":TIM:SCAL?"))
        time_offset = float(device.read(self, ":TIM:OFFS?"))

        print('Time scale: {} time offset: {}ms'.format(time_scale, time_offset))

        for channel in self.active_chan: 
            volt_scale = float(device.read(self, ":" + channel + ":SCAL?"))
            volt_offset = float(device.read(self, ":" + channel + ":OFFS?"))

            print('{} offset value: {} scale value: {}'.format(channel, volt_offset, volt_scale))

            device.write(self, ":WAV:POIN:MODE RAW")
            rawdata = device.read(self, ":WAV:DATA? " + channel)[10:]
            device.write(self, ":KEY:FORCE")

            size = len(rawdata)

            print('Data size: {}'.format(size))

            data = numpy.frombuffer(rawdata, 'B')
            data = data + 255
            data = (data - 130.0 - volt_offset / volt_scale * 25) / 25 * volt_scale
            time = numpy.linspace(time_offset - 6 * time_scale, time_offset + 6 * time_scale, num = len(data))

        #    if time[1] < 1e-3:
        #        time = time * 1e6
        #        tUnit = "uS"
       #     elif time[1] < 1:
       #         time = time * 1e3
       ##         tUnit = "mS"
       #     else:
        #        tUnit = "S"

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

