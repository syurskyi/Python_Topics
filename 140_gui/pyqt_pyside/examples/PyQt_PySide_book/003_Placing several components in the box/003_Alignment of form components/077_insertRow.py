# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("insertRow")
window.resize(300, 150)

lineEdit = QtGui.QLineEdit()
textEdit = QtGui.QTextEdit()
button1 = QtGui.QPushButton("О&тправить")
button2 = QtGui.QPushButton("О&чистить")

hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtGui.QFormLayout()

form.insertRow(0, "&Описание:", textEdit)
form.insertRow(0, "&Название:", lineEdit)
form.insertRow(-1, hbox)

window.setLayout(form)

window.show()
sys.exit(app.exec_())