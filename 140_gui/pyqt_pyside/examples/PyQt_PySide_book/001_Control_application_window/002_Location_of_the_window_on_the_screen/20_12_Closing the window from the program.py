# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("Closing window from program")
window.resize(300, 70)
button = QtGui.QPushButton("Close window", window)
button.setFixedSize(150, 30)
button.move(75, 20)
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       window, QtCore.SLOT("close()"))
window.show()
sys.exit(app.exec_())