# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    s, ok = QtGui.QInputDialog.getItem(window, "Это заголовок окна",
            "Это текст подсказки", ["Пункт 1", "Пункт 2", "Пункт 3"],
            current=1, editable=False)
    if ok:
        print("Текст выбранного пункта:", s)

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