# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    dialog = QtGui.QFileDialog(parent=window,
                               caption="Это заголовок окна")
    dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Нажата кнопка Cancel")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())