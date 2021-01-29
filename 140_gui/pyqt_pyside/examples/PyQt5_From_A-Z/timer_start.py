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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())