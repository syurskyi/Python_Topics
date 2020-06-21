from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()


window.setWindowTitle("Класс QPushButton")
window.resize(300, 80)
button1 = QtGui.QPushButton("Кнопка 1")
button2 = QtGui.QPushButton("Кнопка 2")
button1.setCheckable(True)
button2.setCheckable(True)
button1.setAutoExclusive(True)
button2.setAutoExclusive(True)
mainbox = QtGui.QVBoxLayout()
box = QtGui.QGroupBox("Группа кнопок-переключателей")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
button1.setChecked(True)
