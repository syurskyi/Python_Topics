# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def on_clicked():
    QtWidgets.QMessageBox.information(window, "Текст заголовка",
                                  "Текст сообщения",
                                  buttons=QtWidgets.QMessageBox.Close,
                                  defaultButton=QtWidgets.QMessageBox.Close)

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