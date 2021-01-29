import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Dates", self)
        self.btn.move(40, 40)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfYear())
        print(dt.dayOfWeek())
        print(dt.addDays(23).toString())
        tm = QTime(14, 30, 15)
        print(tm.toString())
        tm2 = tm.addSecs(138)
        print(tm2.toString())
        dtm = QDateTime.currentDateTime()
        print(dtm.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())