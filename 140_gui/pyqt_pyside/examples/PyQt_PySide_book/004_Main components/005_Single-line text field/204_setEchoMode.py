# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 150)
lineEdit1 = QtGui.QLineEdit()
lineEdit2 = QtGui.QLineEdit()
lineEdit3 = QtGui.QLineEdit()
lineEdit4 = QtGui.QLineEdit()
lineEdit1.setEchoMode(QtGui.QLineEdit.Normal)
lineEdit2.setEchoMode(QtGui.QLineEdit.NoEcho)
lineEdit3.setEchoMode(QtGui.QLineEdit.Password)
lineEdit4.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
form = QtGui.QFormLayout()
form.addRow("&Normal:", lineEdit1)
form.addRow("No&Echo:", lineEdit2)
form.addRow("&Password:", lineEdit3)
form.addRow("PasswordEchoOn&Edit:", lineEdit4)
window.setLayout(form)
window.show()
sys.exit(app.exec_())