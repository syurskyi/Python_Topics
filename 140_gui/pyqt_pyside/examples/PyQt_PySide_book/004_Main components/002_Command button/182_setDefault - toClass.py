

def on_clicked_button1():
    print("Нажата кнопка 1")

def on_clicked_button2():
    print("Нажата кнопка 2")

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
line = QtGui.QLineEdit()
button1 = QtGui.QPushButton("Обычная кнопка")
button2 = QtGui.QPushButton("Кнопка по умолчанию")
button1.clicked.connect(on_clicked_button1)
button2.pressed.connect(on_clicked_button2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(line)
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
button1.setAutoDefault(True)
button2.setAutoDefault(True)
button2.setDefault(False)
button2.setDefault(True)
