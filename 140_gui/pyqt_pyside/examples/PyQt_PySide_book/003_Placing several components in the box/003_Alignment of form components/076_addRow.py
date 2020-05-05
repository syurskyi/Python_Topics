# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("addRow")
window.resize(300, 150)

label1 = QtWidgets.QLabel("&Название:")
label2 = QtWidgets.QLabel("&Описание:")
lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("О&тправить")
button2 = QtWidgets.QPushButton("О&чистить")

label1.setBuddy(lineEdit)
label2.setBuddy(textEdit)

hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtWidgets.QFormLayout()
form.addRow(label1, lineEdit)
form.addRow(label2, textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())