# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("insertRow")
window.resize(300, 150)

lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("О&тправить")
button2 = QtWidgets.QPushButton("О&чистить")

hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtWidgets.QFormLayout()

form.insertRow(0, "&Описание:", textEdit)
form.insertRow(0, "&Название:", lineEdit)
form.insertRow(-1, hbox)

window.setLayout(form)

window.show()
sys.exit(app.exec_())