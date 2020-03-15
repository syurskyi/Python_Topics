# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("AlignAbsolute")
window.resize(400, 150)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
button4 = QtGui.QPushButton("4")
button5 = QtGui.QPushButton("5")
button6 = QtGui.QPushButton("6")

window.setLayoutDirection(QtCore.Qt.RightToLeft)
vbox = QtGui.QVBoxLayout()

hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
hbox.addWidget(button3, alignment=QtCore.Qt.AlignLeft)
vbox.addLayout(hbox)

hbox2 = QtGui.QHBoxLayout()
hbox2.addWidget(button4)
hbox2.addWidget(button5)
hbox2.addWidget(button6,
                alignment= QtCore.Qt.AlignAbsolute | QtCore.Qt.AlignLeft)
vbox.addLayout(hbox2)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())