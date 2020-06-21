# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    QtGui.QMessageBox.about(window, "Текст заголовка",
                            "Описание программы")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QMessageBox")
window.resize(300, 70)

ico = window.style().standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
app.setWindowIcon(ico)    # Иконка приложения

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())