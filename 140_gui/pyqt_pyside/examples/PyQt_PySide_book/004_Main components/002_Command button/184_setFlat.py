# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print("Сигнал clicked")

def on_pressed():
    print("Сигнал pressed")

def on_released():
    print("Сигнал released")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Обычная кнопка")
button2 = QtGui.QPushButton("Кнопка Flat")
button2.setFlat(True)
button2.clicked.connect(on_clicked)
button2.pressed.connect(on_pressed)
button2.released.connect(on_released)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())