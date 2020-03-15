# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("QSizePolicy")
window.resize(300, 150)
label = QtGui.QLabel("Текст надписи")
button = QtGui.QPushButton("1")

policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                           QtGui.QSizePolicy.Preferred)
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setSizePolicy(policy)

vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())