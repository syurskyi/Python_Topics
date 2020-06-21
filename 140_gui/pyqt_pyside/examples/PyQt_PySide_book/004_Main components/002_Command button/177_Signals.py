# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print("Сигнал clicked")

def on_pressed():
    print("Сигнал pressed")

def on_released():
    print("Сигнал released")

def on_toggled(status):
    print("Сигнал toggled", status)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Обычная кнопка")
button2 = QtGui.QPushButton("Кнопка-переключатель")
button2.setCheckable(True)
button1.clicked.connect(on_clicked)
button1.pressed.connect(on_pressed)
button1.released.connect(on_released)
button2.toggled["bool"].connect(on_toggled)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())