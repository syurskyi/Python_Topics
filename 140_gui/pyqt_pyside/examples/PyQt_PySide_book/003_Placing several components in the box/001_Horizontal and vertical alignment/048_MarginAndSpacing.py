# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Управление отступами")
window.resize(400, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
button4 = QtGui.QPushButton("4")
button5 = QtGui.QPushButton("5")
button6 = QtGui.QPushButton("6")
vbox = QtGui.QVBoxLayout()

hbox = QtGui.QHBoxLayout()
hbox.setMargin(0)
hbox.setSpacing(0)
hbox.addWidget(button1)
hbox.addWidget(button2)
hbox.addWidget(button3)
vbox.addLayout(hbox)

hbox2 = QtGui.QHBoxLayout()
hbox2.setMargin(30)
hbox2.setSpacing(20)
hbox2.addWidget(button4)
hbox2.addWidget(button5)
hbox2.addWidget(button6)
vbox.addLayout(hbox2)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())