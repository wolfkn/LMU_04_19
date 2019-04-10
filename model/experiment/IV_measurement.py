import time
import numpy as np
import yaml
from model.daq.analog_daq import AnalogDaq

from model import ur


class IVExperiment:
    def __init__(self):
        self.scan_running = False

    def load_config(self, filename):
        with open(filename, 'r') as f:
            self.params = yaml.load(f)

    def load_daq(self):
        port = self.params['Params']['port']
        resistance = ur(self.params['Params']['resistance'])
        self.daq = AnalogDaq(port, resistance)

    def do_scan(self):
        if self.scan_running:
            print('Scan already running')
            return
            # raise Exception("Scan already running")

        self.scan_running = True
        start = ur(self.params['Scan']['start'])
        stop = ur(self.params['Scan']['stop'])
        step = ur(self.params['Scan']['step'])
        self.voltages = np.arange(start.m_as('V'), stop.m_as('V')+step.m_as('V'), step.m_as('V'))
        self.currents = np.zeros((len(self.voltages)))

        for i in range(len(self.voltages)):
            channel = self.params['Scan']['channel_out']
            self.daq.set_voltage(channel, self.voltages[i]*ur('V'))

            channel_in = self.params['Scan']['channel_in']
            current = self.daq.read_current(channel_in)
            self.currents[i] = current.m_as('A')

            delay = ur(self.params['Scan']['delay'])
            time.sleep(delay.m_as('s'))
        self.scan_running = False

    def plot_data(self):
        pass

    def save_data(self, filename):
        np.savetxt(filename, self.currents)

    def save_plot(self, filename):
        pass

    def save_metadata(self, filename):
        with open(filename, 'w') as f:
            yaml.dump(self.params, f)