# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
label = QtGui.QLabel()
label.setText("Текст надписи")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setPixmap(QtGui.QPixmap("foto.png"))
label.setAutoFillBackground(True)
label.setScaledContents(True)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())