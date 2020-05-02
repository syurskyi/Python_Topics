# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_clicked():
    lineEdit.setText("New text")

def on_changed(old_pos, new_pos):
    print("on_changed", old_pos, new_pos)

def on_finished():
    print("on_finished")

def on_return():
    print("on_return")

def on_selection():
    print("on_selection")

def on_text_changed(s):
    print("on_text_changed", s)

def on_text_edited(s):
    print("on_text_edited", s)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLineEdit")
window.resize(300, 100)
lineEdit = QtGui.QLineEdit()
lineEdit.cursorPositionChanged["int","int"].connect(on_changed)
lineEdit.editingFinished.connect(on_finished)
lineEdit.returnPressed.connect(on_return)
lineEdit.selectionChanged.connect(on_selection)
lineEdit.selectionChanged.connect(on_selection)
lineEdit.tC..["const QString&"].connect(on_text_changed)
lineEdit.textEdited["const QString&"].connect(on_text_edited)
lineEdit2 = QtGui.QLineEdit()
button = QtGui.QPushButton("Edit the text programmatically")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(lineEdit2)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())