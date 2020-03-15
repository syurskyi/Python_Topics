


def on_clicked_button1():
    print("Кнопка нажата")


def on_clicked_button2():
    button1.click()

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Кнопка")
button2 = QtGui.QPushButton("Нажми меня")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)

vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
