# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(label.hasSelectedText())
    label.setSelection(3, 10)
    print(label.hasSelectedText())
    print(label.selectedText())
    print(label.selectionStart())
    label.setFocus()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLabel")
window.resize(300, 150)
button = QtGui.QPushButton("Select text")
button.clicked.connect(on_clicked)
label = QtGui.QLabel()
label.setText("This text possible to select")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setFocusPolicy(QtCore.Qt.StrongFocus)
label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())