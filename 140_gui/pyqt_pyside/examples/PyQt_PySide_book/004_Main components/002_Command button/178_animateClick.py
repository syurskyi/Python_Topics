# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked_button1():
    print("Кнопка нажата")


def on_clicked_button2():
    button1.animateClick(500)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Button")
button2 = QtGui.QPushButton("Push me")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())