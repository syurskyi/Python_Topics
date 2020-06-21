# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Текст надписи", flags=QtCore.Qt.Window)
label.setWindowTitle("Класс QLabel")
label.resize(300, 50)
label.show()
sys.exit(app.exec_())