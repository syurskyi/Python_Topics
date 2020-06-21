# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(300, 150)
lcd = QtGui.QLCDNumber(9)
lcd.setSmallDecimalPoint(True)
lcd.display(255.49)
lcd2 = QtGui.QLCDNumber(9)
lcd2.setSmallDecimalPoint(False)
lcd2.display(255.49)
box = QtGui.QVBoxLayout()
box.addWidget(lcd)
box.addWidget(lcd2)
window.setLayout(box)
window.show()
sys.exit(app.exec_())