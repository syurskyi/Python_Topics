import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(400, 400)
        self.cal = QCalendarWidget(self)
        self.cal.move(20, 20)
        self.btn = QPushButton("Get Date", self)
        self.btn.move(130, 200)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = self.cal.selectedDate()
        print(dt)
        print(dt.toJulianDay())
        print(dt.dayOfWeek())
        print(dt.dayOfYear())
        print(dt.daysTo(QDate(2020,7,7)))
        tm = QTime(17, 23, 42)
        print(tm.toString())
        print(tm.secsTo(QTime(19, 34, 12)))
        tmz = QTimeZone(-6*3600)
        print(tmz.country())
        dtm = QDateTime(dt, tm, tmz)
        print(dtm.toString())
        print(dtm.toUTC().toString())
        print(dtm.toSecsSinceEpoch())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())