# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(lcd.value())
    print(lcd.intValue())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(300, 250)
lcd = QtGui.QLCDNumber(9)
lcd.display(255)
button = QtGui.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
button1 = QtGui.QPushButton("Двоичное значение")
button1.clicked.connect(lcd.setBinMode)
button2 = QtGui.QPushButton("Восьмеричное значение")
button2.clicked.connect(lcd.setOctMode)
button3 = QtGui.QPushButton("Десятичное значение")
button3.clicked.connect(lcd.setDecMode)
button4 = QtGui.QPushButton("Шестнадцатеричное значение")
button4.clicked.connect(lcd.setHexMode)
box = QtGui.QVBoxLayout()
box.addWidget(lcd)
box.addWidget(button)
box.addWidget(button1)
box.addWidget(button2)
box.addWidget(button3)
box.addWidget(button4)
window.setLayout(box)
window.show()
sys.exit(app.exec_())