# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по горизонтали")
window.resize(450, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1, 10, QtCore.Qt.AlignRight)
hbox.addWidget(button2, stretch=10)
hbox.addWidget(button3, alignment=QtCore.Qt.AlignRight)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())