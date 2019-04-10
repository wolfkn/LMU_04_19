from PyQt5.QtWidgets import QApplication

from model.experiment.IV_measurement import IVExperiment
from view.scan_window import ScanWindow

exp = IVExperiment()
exp.load_config('Config/experiment.yml')
exp.load_daq()

app = QApplication([])
win = ScanWindow(exp)
win.show()
app.exec()