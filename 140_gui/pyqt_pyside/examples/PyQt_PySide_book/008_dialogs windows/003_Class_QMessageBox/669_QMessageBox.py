# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                               "Текст заголовка", "Текст сообщения",
                               buttons = QtGui.QMessageBox.Ok |
                               QtGui.QMessageBox.Cancel,
                               parent=window)
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