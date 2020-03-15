# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QScrollArea")
window.resize(350, 200)
scrollArea = QtGui.QScrollArea()
widget = QtGui.QWidget()
label1 = QtGui.QLabel("Содержимое компонента 1")
label2 = QtGui.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label1.setMinimumSize(350, 150)
label2.setMinimumHeight(80)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label1)
vbox.addWidget(label2)
widget.setLayout(vbox)
scrollArea.setWidget(widget)
scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

mainbox = QtGui.QVBoxLayout()
mainbox.addWidget(scrollArea)
window.setLayout(mainbox)

window.show()

sys.exit(app.exec_())