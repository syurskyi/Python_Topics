# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по сетке")
window.resize(300, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
grid = QtGui.QGridLayout()
grid.addWidget(button1, 0, 0, alignment=QtCore.Qt.AlignLeft)
grid.addWidget(button2, 0, 1, QtCore.Qt.AlignRight)
grid.addWidget(button3, 1, 0, 1, 2)
window.setLayout(grid)
window.show()
sys.exit(app.exec_())