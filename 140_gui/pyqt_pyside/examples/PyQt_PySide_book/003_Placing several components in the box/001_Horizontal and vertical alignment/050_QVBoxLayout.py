# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по вертикали")
window.resize(300, 150)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
vbox.addWidget(button3)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())