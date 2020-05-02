#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PySide2.QtCore import QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.sGV..(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.sD..()
        self.lbl.setText(date.tS..())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.tS..())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())