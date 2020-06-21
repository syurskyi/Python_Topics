# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    n, ok = QtGui.QInputDialog.getDouble(window, "Это заголовок окна",
                                         "Это текст подсказки",
                                         value=50.0, min=0.0, max=100.0,
                                         decimals=2)
    if ok:
        print("Введено значение:", n)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QInputDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())