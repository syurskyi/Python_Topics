# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена иконки в заголовке окна")
window.resize(300, 100)
ico = QtGui.QIcon("Camera.png")
window.setWindowIcon(ico)             # Иконка для окна
app.setWindowIcon(ico)                # Иконка приложения
window.show()
sys.exit(app.exec_())