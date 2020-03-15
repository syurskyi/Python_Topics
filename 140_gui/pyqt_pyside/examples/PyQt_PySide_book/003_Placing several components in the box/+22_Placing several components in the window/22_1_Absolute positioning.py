# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Absolute positioning")
window.resize(300, 120)
label = QtGui.QLabel("The text of the inscription", window)
button = QtGui.QPushButton("The text on the button", window)
label.setGeometry(10, 10, 280, 60)
button.resize(280, 30)
button.move(10, 80)
window.show()
sys.exit(app.exec_())