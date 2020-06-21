# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(lineEdit.text(), lineEdit2.text())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 50)
lineEdit = QtGui.QLineEdit()
lineEdit.setPlaceholderText("Enter login")
lineEdit2 = QtGui.QLineEdit()
lineEdit2.setPlaceholderText("Enter password")
lineEdit2.setEchoMode(QtGui.QLineEdit.Password)
button = QtGui.QPushButton("OK")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(lineEdit2)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())