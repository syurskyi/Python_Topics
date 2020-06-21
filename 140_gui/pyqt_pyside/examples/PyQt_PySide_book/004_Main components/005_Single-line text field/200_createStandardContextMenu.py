# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_mypaste():
    lineEdit.insert("my text")

class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)

    def contextMenuEvent(self, e):
        menu = self.createStandardContextMenu()
        menu.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        menu.addSeparator()
        menu.addAction("New item", on_mypaste, "Ctrl+M")
        menu.exec_(e.globalPos())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 50)
lineEdit = MyLineEdit()
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec_())