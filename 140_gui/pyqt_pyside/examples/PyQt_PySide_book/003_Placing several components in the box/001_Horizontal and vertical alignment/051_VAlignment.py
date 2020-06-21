# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Выравнивание по вертикали")
window.resize(300, 150)
button1 = QtWidgets.QPushButton("Bottom")
button2 = QtWidgets.QPushButton("No")
button3 = QtWidgets.QPushButton("Top")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1, alignment=QtCore.Qt.AlignBottom)
vbox.addWidget(button2)
vbox.addWidget(button3, alignment=QtCore.Qt.AlignTop)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())