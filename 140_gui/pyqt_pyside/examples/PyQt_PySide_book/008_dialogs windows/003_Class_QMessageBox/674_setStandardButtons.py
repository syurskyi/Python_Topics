# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_button_clicked(btn):
    if btn:
        print(btn.text())

def on_clicked():
    dialog = QtGui.QMessageBox(parent=window)
    dialog.setIcon(QtGui.QMessageBox.Critical)
    dialog.setWindowTitle("Текст заголовка")
    dialog.setText("Текст <b>сообщения</b><br>на двух строках")
    dialog.setInformativeText("Поясняющий <b>текст</b>")
    dialog.setDetailedText("Описание деталей")
    dialog.setStandardButtons(QtGui.QMessageBox.Ok |
                              QtGui.QMessageBox.Cancel)
    dialog.setDefaultButton(QtGui.QMessageBox.Cancel)
    dialog.setEscapeButton(QtGui.QMessageBox.Cancel)
    dialog.buttonClicked["QAbstractButton *"].connect(on_button_clicked)
    result = dialog.exec_()
    if result == QtGui.QMessageBox.Ok:
        print("Нажата кнопка OK")
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