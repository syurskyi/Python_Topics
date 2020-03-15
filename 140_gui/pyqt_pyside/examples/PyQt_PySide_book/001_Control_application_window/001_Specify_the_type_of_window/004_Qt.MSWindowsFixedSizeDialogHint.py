# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowFlags(QtCore.Qt.Window |
                      QtCore.Qt.MSWindowsFixedSizeDialogHint)
window.setWindowTitle("Window title")
window.resize(300, 70)
btn = QtGui.QPushButton("Close window", window)
btn.setGeometry(50, 10, 200, 30)
QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), app.quit)
desktop = QtGui.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec_())