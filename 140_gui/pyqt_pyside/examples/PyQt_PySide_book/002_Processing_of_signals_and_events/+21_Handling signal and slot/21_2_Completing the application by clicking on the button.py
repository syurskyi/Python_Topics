# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Complete work")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       app,    QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())