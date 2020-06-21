# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 50)
lineEdit = QtGui.QLineEdit("Default Text")
lineEdit.insert("New text!")
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec_())