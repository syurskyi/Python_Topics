# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    cur.beginEditBlock()              # Начало блока
    cur.insertHtml("<b>inserted fragment 1</b>")
    cur.insertHtml("""<span style="color: red;">inserted fragment 2</span>""")
    cur.endEditBlock()                # Конец блока
    textEdit.setTextCursor(cur)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setHtml("<p>Block 1</p><p>Block 2</p>")
button = QtGui.QPushButton("Insert text")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())