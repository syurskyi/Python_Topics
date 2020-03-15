from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QLabel")
window.resize(300, 80)
label = QtGui.QLabel("&Пароль")
lineEdit = QtGui.QLineEdit()
label.setBuddy(lineEdit)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(lineEdit)
vbox.addWidget(QtGui.QLineEdit())
window.setLayout(vbox)
