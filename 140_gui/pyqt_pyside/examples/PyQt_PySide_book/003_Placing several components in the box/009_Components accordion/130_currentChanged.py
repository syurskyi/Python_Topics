# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_current_changed(index):
    print("on_current_changed", index)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QToolBox")
window.resize(300, 250)
toolBox = QtGui.QToolBox()
toolBox.currentChanged["int"].connect(on_current_changed)
toolBox.addItem(QtGui.QLabel("Content tab 1"), "inset &1")
toolBox.addItem(QtGui.QLabel("Content tab 2"), "inset &2")
toolBox.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())