# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print("Кнопка нажата")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 80)
button = QtGui.QPushButton("Кнопка")
button.clicked.connect(on_clicked)
button.setAutoRepeat(True)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())