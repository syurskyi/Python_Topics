# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 80)
label = QtGui.QLabel("&Пароль")
lineEdit = QtGui.QLineEdit()
label.setBuddy(lineEdit)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(lineEdit)
vbox.addWidget(QtGui.QLineEdit())
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())