# -*- coding: utf-8 -*-
from PySide import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Change the window title icon")
window.resize(300, 100)
window.setWindowIcon(QtGui.QIcon("Camera.png")) # Иконка для окна
app.setWindowIcon(QtGui.QIcon("NukeApp128.png"))    # Иконка приложения
window.show()
sys.exit(app.exec_())