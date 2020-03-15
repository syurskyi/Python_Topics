# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(lineEdit.text())
    lineEdit.setSelection(0, 6)
    print(lineEdit.selectedText())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 50)
lineEdit = QtGui.QLineEdit()
button = QtGui.QPushButton("Get value")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())