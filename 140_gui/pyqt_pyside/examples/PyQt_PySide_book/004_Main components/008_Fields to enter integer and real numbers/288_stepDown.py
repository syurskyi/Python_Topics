# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    spinBox.stepDown()

def on_clicked2():
    spinBox.stepUp()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QSpinBox")
window.resize(300, 70)
spinBox = QtGui.QSpinBox()
spinBox.setRange(0, 100)
button = QtGui.QPushButton("-")
button.clicked.connect(on_clicked)
button2 = QtGui.QPushButton("+")
button2.clicked.connect(on_clicked2)
box = QtGui.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec_())