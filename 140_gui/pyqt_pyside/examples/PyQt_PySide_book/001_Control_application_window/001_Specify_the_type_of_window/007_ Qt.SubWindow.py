# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.SubWindow)
window.setWindowTitle("Заголовок окна")
window.resize(300, 70)
btn = QtWidgets.QPushButton("Закрыть окно", window)
btn.setGeometry(50, 10, 200, 30)
btn.clicked.connect(app.quit)
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec_())