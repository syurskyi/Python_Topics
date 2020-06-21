# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    if lineEdit.hasAcceptableInput():
        print(lineEdit.text())
    else:
        print("The value does not match the mask")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 50)
lineEdit = QtGui.QLineEdit()
lineEdit.setInputMask("Date: 99.B9.9999;#")
button = QtGui.QPushButton("Get Value")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())