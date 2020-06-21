# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Display the window in the center of the screen")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.frameSize().width()) // 2
y = (desktop.height() - window.frameSize().height()) // 2
window.move(x, y)
sys.exit(app.exec_())