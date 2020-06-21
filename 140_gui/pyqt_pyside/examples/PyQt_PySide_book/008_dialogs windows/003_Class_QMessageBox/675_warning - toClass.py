# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    result = QtGui.QMessageBox.warning(window, "Текст заголовка",
                   "Действие может быть опасным. Продолжить?",
                   buttons=QtGui.QMessageBox.Yes | QtGui.QMessageBox.No |
                   QtGui.QMessageBox.Cancel,
                   defaultButton=QtGui.QMessageBox.Cancel)
    if result == QtGui.QMessageBox.Yes:
        print("Нажата кнопка Yes")
    elif result == QtGui.QMessageBox.No:
        print("Нажата кнопка No")
    elif result == QtGui.QMessageBox.Cancel:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>")
    else:
        print("Нажата кнопка", result)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QMessageBox")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())