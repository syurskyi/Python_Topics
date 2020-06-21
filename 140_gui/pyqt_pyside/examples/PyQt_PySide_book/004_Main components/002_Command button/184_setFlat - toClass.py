

def on_clicked():
    print("Сигнал clicked")

def on_pressed():
    print("Сигнал pressed")

def on_released():
    print("Сигнал released")

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

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
