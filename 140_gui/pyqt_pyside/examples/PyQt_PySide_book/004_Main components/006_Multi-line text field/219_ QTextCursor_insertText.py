# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    cur.beginEditBlock()              # Начало блока
    cur.insertText("New Block 1\n")
    cur.insertText("New Block 2\n")
    cur.endEditBlock()                # Конец блока
    cur.joinPreviousEditBlock()       # Продолжение предыдущего блока
    cur.insertText("New Block 3\n")
    cur.endEditBlock()                # Конец блока
    textEdit.setTextCursor(cur)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5")
button = QtGui.QPushButton("Insert text")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())