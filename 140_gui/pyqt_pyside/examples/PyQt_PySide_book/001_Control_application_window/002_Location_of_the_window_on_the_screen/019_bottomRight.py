# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна в нижнем правом углу экрана")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()
desktop = QtWidgets.QApplication.desktop()
taskBarHeight = (desktop.screenGeometry().height() -
                 desktop.availableGeometry().height())
x = desktop.width() - window.frameSize().width()
y = desktop.height() - window.frameSize().height() - taskBarHeight
window.move(x, y)
sys.exit(app.exec_())