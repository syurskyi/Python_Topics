# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.cursorForPosition(QtCore.QPoint(100, 5))
    textEdit.setTextCursor(cur)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Default value")
button = QtGui.QPushButton("Set the cursor")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())