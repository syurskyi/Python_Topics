import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(400, 100)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.display(125)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("background-color:black;color:green")
        self.lcd.setBinMode()

        self.lytMain = QHBoxLayout()
        self.lytMain.addWidget(self.lcd)
        self.setLayout(self.lytMain)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
