# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("addStretch")
window.resize(350, 50)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addStretch(1)
hbox.addWidget(button2)
hbox.addWidget(button3)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())