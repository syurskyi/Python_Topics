import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(600, 200)

        self.lytMain = QVBoxLayout()
        self.lytButtons = QHBoxLayout()
        self.lytLCD = QHBoxLayout()
        self.lytMain.addLayout(self.lytButtons)
        self.lytMain.addLayout(self.lytLCD)
        self.setLayout(self.lytMain)

        self.lcd = QLCDNumber(10)
        self.lcd.setStyleSheet("background-color:black; color:green")
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(0)
        self.lcd.overflow.connect(self.evt_lcd_overflow)

        self.sld = QSlider(Qt.Vertical)
        self.sld.setTickPosition(QSlider.TicksBothSides)
        self.sld.setTickInterval(20)
        self.sld.valueChanged.connect(self.evt_sld_valueChanged)

        self.dial = QDial()
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setNotchTarget(10)
        self.dial.valueChanged.connect(self.evt_sld_valueChanged)


        self.rbtDec = QRadioButton("Dec")
        self.rbtDec.setChecked(True)
        self.rbtDec.clicked.connect(self.evt_rbt_clicked)

        self.rbtHex = QRadioButton("Hex")
        self.rbtHex.clicked.connect(self.evt_rbt_clicked)

        self.rbtOct = QRadioButton("Oct")
        self.rbtOct.clicked.connect(self.evt_rbt_clicked)

        self.rbtBin = QRadioButton("Bin")
        self.rbtBin.clicked.connect(self.evt_rbt_clicked)

        self.lytLCD.addWidget(self.sld)
        self.lytLCD.addWidget(self.dial)
        self.lytLCD.addWidget(self.lcd)
        self.lytButtons.addWidget(self.rbtDec)
        self.lytButtons.addWidget(self.rbtHex)
        self.lytButtons.addWidget(self.rbtOct)
        self.lytButtons.addWidget(self.rbtBin)

    def evt_rbt_clicked(self):
        sender = self.sender()
        print(sender.text())
        if sender.text() == "Dec":
            self.lcd.setDecMode()
        elif sender.text() == "Hex":
            self.lcd.setHexMode()
        elif sender.text() == "Oct":
            self.lcd.setOctMode()
        elif sender.text() == "Bin":
            self.lcd.setBinMode()

    def evt_lcd_overflow(self):
        QMessageBox.warning(self, "Overflow", "You have an overflow error")

    def evt_sld_valueChanged(self, val):
        self.lcd.display(val)
        self.sld.setValue(val)
        self.dial.setValue(val)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())