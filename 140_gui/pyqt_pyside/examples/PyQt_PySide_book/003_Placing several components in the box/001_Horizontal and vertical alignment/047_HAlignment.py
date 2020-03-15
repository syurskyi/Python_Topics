# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по горизонтали")
window.resize(400, 50)
button1 = QtGui.QPushButton("Right")
button2 = QtGui.QPushButton("No")
button3 = QtGui.QPushButton("Left")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1, alignment=QtCore.Qt.AlignRight)
hbox.addWidget(button2)
hbox.addWidget(button3, alignment=QtCore.Qt.AlignLeft)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())