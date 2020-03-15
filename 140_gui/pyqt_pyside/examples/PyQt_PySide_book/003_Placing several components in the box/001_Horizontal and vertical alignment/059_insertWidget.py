# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по горизонтали")
window.resize(300, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button3 = QtGui.QPushButton("3")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.insertWidget(-1, button2) # Добавление в конец
hbox.insertWidget(0, button3)  # Добавление в начало
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())