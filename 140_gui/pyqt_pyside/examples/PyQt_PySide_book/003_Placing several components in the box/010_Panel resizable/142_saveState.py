# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

state = None

def on_clicked_button1():
    global state
    state = splitter.saveState()
    button2.setEnabled(True)

def on_clicked_button2():
    global state
    splitter.restoreState(state)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QSplitter")
window.resize(300, 350)
button1 = QtGui.QPushButton("Запомнить размеры")
button2 = QtGui.QPushButton("Восстановить размеры")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)
button2.setEnabled(False)
splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
label1 = QtGui.QLabel("Содержимое компонента 1")
label2 = QtGui.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(splitter)
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())