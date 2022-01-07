# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui,QtWidgets
import sys

def on_clicked():
    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                               "Текст заголовка", "Текст сообщения",
                               buttons = QtWidgets.QMessageBox.Ok |
                               QtWidgets.QMessageBox.Cancel,
                               parent=window)
    result = dialog.exec_()
    if result == QtWidgets.QMessageBox.Ok:
        print("Нажата кнопка OK")
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