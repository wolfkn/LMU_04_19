import serial
import time
import pint

ur = pint.UnitRegistry()

class Device:
    def __init__(self, port):
        self.port = port
        self.rsc = None

    def initialize(self):
        self.rsc = serial.Serial(self.port)
        time.sleep(1)

    def idn(self):
        if self.rsc is None:
            raise Exception('Device not initialized yet.')

        self.rsc.write(b'IDN\n')
        answer = self.rsc.readline()
        return answer

    def set_analog_out(self, channel, value):
        command = 'OUT:CH{}:{}\n'.format(channel, value)
        self.rsc.write(command.encode('utf-8'))
        time.sleep(0.05)

    def get_analog_in(self, channel):
        command = 'IN:CH{}\n'.format(channel)
        self.rsc.write(command.encode('utf-8'))
        answer = self.rsc.readline()
        answer = answer.strip()
        answer = answer.decode()
        answer = int(answer)
        # transform answer to voltage
        # transform answer to current
        return answer

    def finalize(self):
        pass


dev = Device('/dev/ttyACM0')
dev.initialize()
idn = dev.idn()
print('IDN: {}'.format(idn))
voltages = [i for i in range(4095) if i%100==0]
currents = []
for v in voltages:
    dev.set_analog_out(0, v)
    currents.append(dev.get_analog_in(0))

print(currents)
current = currents[-1]
current_v = current/1024*3.3 * ur('V')
current_a = current_v/(220*ur('ohm'))
print('The current is {}'.format(current_a.to('mA')))