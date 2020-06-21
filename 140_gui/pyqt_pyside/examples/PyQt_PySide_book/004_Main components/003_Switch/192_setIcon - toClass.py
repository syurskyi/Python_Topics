

def on_toggled_radio1(status):
    print("radio1", status)

def on_toggled_radio2(status):
    print("radio2", status)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QRadioButton")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("&Да")
radio2 = QtGui.QRadioButton("&Нет")
style = window.style()
icon1 = style.standardIcon(QtGui.QStyle.SP_DialogOkButton)
radio1.setIcon(icon1)
icon2 = style.standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
radio2.setIcon(icon2)

mainbox = QtGui.QVBoxLayout()
radio1.toggled["bool"].connect(on_toggled_radio1)
radio2.toggled["bool"].connect(on_toggled_radio2)
box = QtGui.QGroupBox("&Вы знаете язык Python?")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)

