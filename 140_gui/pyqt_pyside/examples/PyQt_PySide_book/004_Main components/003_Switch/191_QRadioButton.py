# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_toggled_radio1(status):
    print("radio1", status)

def on_toggled_radio2(status):
    print("radio2", status)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QRadioButton")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("&Да")
radio2 = QtGui.QRadioButton("&Нет")
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
window.show()
sys.exit(app.exec_())