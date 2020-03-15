# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    print(cur.movePosition(QtGui.QTextCursor.NextCharacter,
                           mode=QtGui.QTextCursor.MoveAnchor, n=10))
    textEdit.setTextCursor(cur)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5 jjkh hkjhkjh khk hkh khk jhkh hkh khk hk hkh hkj hk hkhk k kjh kh jh kh khk hkh khk hkjh kh kh kjh kjhkj h kh kh kjh khk hk kh kh k")
button = QtGui.QPushButton("Move the cursor 10 characters ahead")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())