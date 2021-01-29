import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lytMain = QHBoxLayout()
        self.setLayout(self.lytMain)

        self.lblColor = QLabel()
        self.pxm = QPixmap(50, 50)
        self.lstColor = ["red", "green", "blue", "yellow", "violet", "black", "white"]
        self.pxm.fill(QColor(random.choice(self.lstColor)))
        self.lblColor.setPixmap(self.pxm)
        self.lytMain.addWidget(self.lblColor)

        self.btnStart = QPushButton("Start")
        self.lytMain.addWidget(self.btnStart)

        self.btnStop = QPushButton("Stop")
        self.lytMain.addWidget(self.btnStop)

        self.tmr = QTimer()
        self.tmr.timeout.connect(self.evt_tmr_timeout)

        self.btnStart.clicked.connect(self.evt_btnStart_clicked)
        self.btnStop.clicked.connect(self.evt_btnStop_clicked)

        #######  Challenge code

        self.slider = QSlider()
        self.slider.setMaximum(1000)
        self.slider.setValue(500)
        self.lytMain.addWidget(self.slider)
        self.slider.valueChanged.connect(self.evt_slider_changed)

    def evt_slider_changed(self, val):
        self.tmr.setInterval(val)

        ####### End of challenge code

    def evt_btnStart_clicked(self):
        self.tmr.start(500)

    def evt_btnStop_clicked(self):
        self.tmr.stop()

    def evt_tmr_timeout(self):
        clr = random.choice(self.lstColor)
        print(clr)
        self.pxm.fill(QColor(clr))
        self.lblColor.setPixmap(self.pxm)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())