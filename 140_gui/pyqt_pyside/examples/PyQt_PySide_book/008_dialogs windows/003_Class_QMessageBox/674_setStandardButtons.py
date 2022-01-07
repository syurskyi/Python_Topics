# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def on_button_clicked(btn):
    if btn:
        print(btn.text())

def on_clicked():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setIcon(QtWidgets.QMessageBox.Critical)
    dialog.setWindowTitle("Текст заголовка")
    dialog.setText("Текст <b>сообщения</b><br>на двух строках")
    dialog.setInformativeText("Поясняющий <b>текст</b>")
    dialog.setDetailedText("Описание деталей")
    dialog.setStandardButtons(QtWidgets.QMessageBox.Ok |
                              QtWidgets.QMessageBox.Cancel)
    dialog.setDefaultButton(QtWidgets.QMessageBox.Cancel)
    dialog.setEscapeButton(QtWidgets.QMessageBox.Cancel)
    dialog.buttonClicked["QAbstractButton *"].connect(on_button_clicked)
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