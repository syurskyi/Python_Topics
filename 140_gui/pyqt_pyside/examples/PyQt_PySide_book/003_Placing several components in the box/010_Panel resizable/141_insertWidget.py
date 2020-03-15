# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    splitter.insertWidget(0, label3)
    button.setEnabled(False)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QSplitter")
window.resize(300, 350)
button = QtGui.QPushButton("Добавить компонент")
button.clicked.connect(on_clicked)
splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
label1 = QtGui.QLabel("Содержимое компонента 1")
label2 = QtGui.QLabel("Содержимое компонента 2")
label3 = QtGui.QLabel("Содержимое компонента 3")
label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label3.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(splitter)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())