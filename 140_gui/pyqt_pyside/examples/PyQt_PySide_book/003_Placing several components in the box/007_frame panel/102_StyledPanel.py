# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QFrame. StyledPanel")
window.resize(300, 250)
frame1 = QtGui.QFrame()
frame2 = QtGui.QFrame()
frame3 = QtGui.QFrame()
frame1.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Plain)
frame2.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Raised)
frame3.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(frame1)
vbox.addWidget(frame2)
vbox.addWidget(frame3)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())