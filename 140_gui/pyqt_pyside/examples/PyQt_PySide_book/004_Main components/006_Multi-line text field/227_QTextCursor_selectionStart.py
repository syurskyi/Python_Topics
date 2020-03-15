# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    if cur.hasSelection():
        print(cur.selectionStart(), cur.selectionEnd())
    else:
        print("Nothing selected")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5")
button = QtGui.QPushButton("Select the fragment before the beginning of the document")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())