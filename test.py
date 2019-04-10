import threading
from model.experiment.IV_measurement import IVExperiment


exp = IVExperiment()
exp.load_config('Config/experiment.yml')
print(exp.params)
exp.load_daq()
exp.params['Scan']['step'] = '500mV'
print('Beginning scan')

t = threading.Thread(target=exp.do_scan)
t.start()
print('Scan started')
while t.is_alive():
    print('Still running')

exp.save_data('test.dat')
exp.save_metadata('test_metadata.yml')