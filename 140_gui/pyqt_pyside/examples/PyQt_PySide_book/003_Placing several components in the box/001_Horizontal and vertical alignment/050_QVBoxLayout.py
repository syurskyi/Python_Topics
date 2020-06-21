# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Выравнивание по вертикали")
window.resize(300, 150)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
vbox.addWidget(button3)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())