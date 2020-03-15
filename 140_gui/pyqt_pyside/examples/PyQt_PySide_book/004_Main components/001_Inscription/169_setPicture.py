# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(500, 350)
label = QtGui.QLabel()
picture = QtGui.QPicture()
painter = QtGui.QPainter()
painter.begin(picture)
painter.fillRect(10, 10, 480, 330, QtGui.QBrush(QtCore.Qt.white))
painter.end()
label.setPicture(picture)
label.setAutoFillBackground(True)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())