# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    (n, ok) = QtGui.QColorDialog.getRgba(
              initial=QtGui.QColor("#ff0000").rgba(), parent=window)
    if ok:
        color = QtGui.QColor.fromRgba(n)
        print(color.red(), color.green(), color.blue(), color.alpha())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QColorDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())