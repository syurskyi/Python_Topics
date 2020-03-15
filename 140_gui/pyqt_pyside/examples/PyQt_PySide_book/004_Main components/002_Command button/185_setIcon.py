# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked():
    print("Кнопка нажата")


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button = QtGui.QPushButton()
style = window.style()
icon = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
button.setIcon(icon)
button.setIconSize(QtCore.QSize(32, 32))
button.clicked.connect(on_clicked)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())