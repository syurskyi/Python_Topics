# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtWidgets
import sys

def on_clicked():
    result = QtWidgets.QMessageBox.warning(window, "Текст заголовка",
                   "Действие может быть опасным. Продолжить?",
                   buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
                   QtWidgets.QMessageBox.Cancel,
                   defaultButton=QtWidgets.QMessageBox.Cancel)
    if result == QtWidgets.QMessageBox.Yes:
        print("Нажата кнопка Yes")
    elif result == QtWidgets.QMessageBox.No:
        print("Нажата кнопка No")
    elif result == QtWidgets.QMessageBox.Cancel:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>")
    else:
        print("Нажата кнопка", result)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QMessageBox")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())