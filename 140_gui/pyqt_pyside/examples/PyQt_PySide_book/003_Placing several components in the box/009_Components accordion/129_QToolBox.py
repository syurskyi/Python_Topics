# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QToolBox")
window.resize(300, 150)
toolBox = QtGui.QToolBox()
toolBox.addItem(QtGui.QLabel("Content tab 1"), "inset &1")
toolBox.addItem(QtGui.QLabel("Content tab 2"), "inset &2")
toolBox.addItem(QtGui.QLabel("Content tab 3"), "inset &3")
toolBox.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
