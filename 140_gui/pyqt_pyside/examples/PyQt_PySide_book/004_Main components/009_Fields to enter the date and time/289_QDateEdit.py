# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys, datetime

def on_clicked():
    print(dateTimeEdit.date().toPyDate())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QDateEdit")
window.resize(300, 70)
dt = datetime.datetime.today()
delta = datetime.timedelta(days=365)
dt_min = dt - delta
dt_max = dt + delta
dateTimeEdit = QtGui.QDateEdit(dt.date())
dateTimeEdit.setDateRange(dt_min.date(), dt_max.date())
dateTimeEdit.setCalendarPopup(True)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())