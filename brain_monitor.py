import sys
import numpy as np
from PyQt6 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg

class EEGMonitor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.setWindowTitle("NeuroLink | Advanced EEG Real-Time Monitor")
        self.resize(1100, 700)
        self.setStyleSheet("background-color: #0f172a; color: #f8fafc;")

        # --- Main Layout ---
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Header
        self.header = QtWidgets.QLabel("LIVE EEG DATA ARCHIVE - PATIENT ID: #2006-05-06")
        self.header.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Weight.Bold))
        self.header.setStyleSheet("color: #38bdf8; margin-bottom: 10px;")
        self.layout.addWidget(self.header)

        # --- Plotting Setup ---
        # We use a GraphicsLayoutWidget for high-performance plotting
        self.win = pg.GraphicsLayoutWidget()
        self.layout.addWidget(self.win)

        # EEG Channels Settings
        self.n_channels = 3
        self.points_to_show = 500  # Number of points visible on screen
        self.data = [np.zeros(self.points_to_show) for _ in range(self.n_channels)]
        self.plots = []
        self.curves = []

        colors = ['#38bdf8', '#10b981', '#fbbf24']  # Blue, Green, Amber
        names = ["Channel Fp1 (Frontal)", "Channel C3 (Central)", "Channel O1 (Occipital)"]

        for i in range(self.n_channels):
            p = self.win.addPlot(row=i, col=0)
            p.setLabel('left', names[i], units='μV', color=colors[i])
            p.showGrid(x=True, y=True, alpha=0.3)
            p.setYRange(-50, 50)
            
            curve = p.plot(pen=pg.mkPen(colors[i], width=2))
            self.plots.append(p)
            self.curves.append(curve)

        # --- Status Bar ---
        self.info_panel = QtWidgets.QHBoxLayout()
        self.status = QtWidgets.QLabel("STATUS: ACTIVE MONITORING")
        self.status.setStyleSheet("color: #ef4444; font-weight: bold;")
        self.info_panel.addWidget(self.status)
        
        self.freq_label = QtWidgets.QLabel("Sampling: 512Hz | Impedance: <5kΩ")
        self.info_panel.addWidget(self.freq_label, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.layout.addLayout(self.info_panel)

        # --- Data Update Timer ---
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(30)  # Updates every 30ms

        self.phase = 0

    def update_data(self):
        self.phase += 0.1
        
        for i in range(self.n_channels):
            # Shift data to the left
            self.data[i][:-1] = self.data[i][1:]
            
            # Generate "Realistic" EEG Signal
            # Combination of sine waves (brain rhythms) + random noise
            noise = np.random.normal(0, 2)
            alpha_wave = 15 * np.sin(self.phase * (i + 1) * 0.8) 
            beta_wave = 5 * np.sin(self.phase * 5)
            
            new_point = alpha_wave + beta_wave + noise
            self.data[i][-1] = new_point
            
            # Update the plot curve
            self.curves[i].setData(self.data[i])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    monitor = EEGMonitor()
    monitor.show()
    sys.exit(app.exec())
