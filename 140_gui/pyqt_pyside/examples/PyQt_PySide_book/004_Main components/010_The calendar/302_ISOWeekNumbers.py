# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys, datetime

def on_clicked():
    print(calendar.sD..().toPyDate())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QCalendarWidget")
window.resize(300, 200)
calendar = QtGui.QCalendarWidget()
calendar.setSelectedDate(datetime.date.today())
calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
calendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.ISOWeekNumbers)
button = QtGui.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())