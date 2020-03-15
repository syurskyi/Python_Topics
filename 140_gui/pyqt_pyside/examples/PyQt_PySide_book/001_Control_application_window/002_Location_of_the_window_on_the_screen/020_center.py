# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Display the window in the center of the screen")
window.resize(300, 100)
desktop = QtGui.QApplication.desktop()
window.move(desktop.availableGeometry().center() -
            window.rect().center())
window.show()
sys.exit(app.exec_())