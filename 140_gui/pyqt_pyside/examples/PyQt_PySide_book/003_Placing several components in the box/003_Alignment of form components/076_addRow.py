# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("addRow")
window.resize(300, 150)

label1 = QtGui.QLabel("&Название:")
label2 = QtGui.QLabel("&Описание:")
lineEdit = QtGui.QLineEdit()
textEdit = QtGui.QTextEdit()
button1 = QtGui.QPushButton("О&тправить")
button2 = QtGui.QPushButton("О&чистить")

label1.setBuddy(lineEdit)
label2.setBuddy(textEdit)

hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtGui.QFormLayout()
form.addRow(label1, lineEdit)
form.addRow(label2, textEdit)
form.addRow(hbox)
window.setLayout(form)

window.show()
sys.exit(app.exec_())