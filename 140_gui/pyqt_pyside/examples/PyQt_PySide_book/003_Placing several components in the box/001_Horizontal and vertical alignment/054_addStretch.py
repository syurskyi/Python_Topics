# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("addStretch")
window.resize(350, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addStretch(1)
hbox.addWidget(button2)
hbox.addWidget(button3)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())