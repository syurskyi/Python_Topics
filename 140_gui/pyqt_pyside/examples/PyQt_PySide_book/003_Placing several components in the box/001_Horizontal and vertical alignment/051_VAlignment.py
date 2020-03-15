# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по вертикали")
window.resize(300, 150)
button1 = QtGui.QPushButton("Bottom")
button2 = QtGui.QPushButton("No")
button3 = QtGui.QPushButton("Top")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1, alignment=QtCore.Qt.AlignBottom)
vbox.addWidget(button2)
vbox.addWidget(button3, alignment=QtCore.Qt.AlignTop)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())