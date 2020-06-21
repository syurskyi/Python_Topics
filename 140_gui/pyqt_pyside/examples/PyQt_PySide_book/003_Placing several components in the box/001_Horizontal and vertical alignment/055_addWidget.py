# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Выравнивание по горизонтали")
window.resize(450, 50)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1, 10, QtCore.Qt.AlignRight)
hbox.addWidget(button2, stretch=10)
hbox.addWidget(button3, alignment=QtCore.Qt.AlignRight)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())