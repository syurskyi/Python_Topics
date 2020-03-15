# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("WrapLongRows")
window.resize(300, 150)
lineEdit = QtGui.QLineEdit()
textEdit = QtGui.QTextEdit()
button1 = QtGui.QPushButton("О&тправить")
button2 = QtGui.QPushButton("О&чистить")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtGui.QFormLayout()
form.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
form.addRow("&Название литературного или другого произведения:", lineEdit)
form.addRow("&Описание:", textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())