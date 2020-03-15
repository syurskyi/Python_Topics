# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Display window in the lower right corner of the screen")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()
desktop = QtGui.QApplication.desktop()
taskBarHeight = (desktop.screenGeometry().height() -
                 desktop.availableGeometry().height())
x = desktop.width() - window.frameSize().width()
y = desktop.height() - window.frameSize().height() - taskBarHeight
window.move(x, y)
sys.exit(app.exec_())
