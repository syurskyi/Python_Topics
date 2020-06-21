

def on_state_changed1(status):
    print("checkBox1", status)

def on_state_changed2(status):
    print("checkBox2", status)

def on_state_changed3(status):
    print("checkBox2", status)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QCheckBox")
window.resize(300, 150)
checkBox1 = QtGui.QCheckBox("&Unchecked")
checkBox2 = QtGui.QCheckBox("&PartiallyChecked")
checkBox3 = QtGui.QCheckBox("&Checked")
checkBox2.setTristate(True)
checkBox1.setCheckState(QtCore.Qt.Unchecked)
checkBox2.setCheckState(QtCore.Qt.PartiallyChecked)
checkBox3.setCheckState(QtCore.Qt.Checked)
style = window.style()
icon1 = style.standardIcon(QtGui.QStyle.SP_DialogOkButton)
checkBox1.setIcon(icon1)
icon2 = style.standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
checkBox2.setIcon(icon2)
checkBox1.stateChanged["int"].connect(on_state_changed1)
checkBox1.toggled["bool"].connect(on_state_changed1)
checkBox2.stateChanged["int"].connect(on_state_changed2)
checkBox3.stateChanged["int"].connect(on_state_changed3)
box = QtGui.QVBoxLayout()
box.addWidget(checkBox1)
box.addWidget(checkBox2)
box.addWidget(checkBox3)
window.setLayout(box)
