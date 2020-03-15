# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Вложение контейнеров")
window.resize(300, 150)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
button4 = QtGui.QPushButton("4")
button5 = QtGui.QPushButton("5")
button6 = QtGui.QPushButton("6")

vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
vbox.addWidget(button3)

hbox = QtGui.QHBoxLayout()
hbox.addWidget(button4)
hbox.addWidget(button5)
hbox.addWidget(button6)

vbox.addLayout(hbox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())