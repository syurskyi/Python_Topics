# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Выравнивание по сетке")
window.resize(300, 50)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button4 = QtWidgets.QPushButton("4")
grid = QtWidgets.QGridLayout()
grid.addWidget(button1, 0, 0, 2, 1)
grid.addWidget(button2, 0, 1)
grid.addWidget(button4, 1, 1)
window.setLayout(grid)
window.show()
sys.exit(app.exec_())