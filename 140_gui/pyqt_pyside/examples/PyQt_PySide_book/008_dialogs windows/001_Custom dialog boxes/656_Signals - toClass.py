# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle("Диалоговое окно")
        self.resize(200, 70)

        self.mainBox = QtGui.QVBoxLayout()

        self.lineEdit = QtGui.QLineEdit()
        self.mainBox.addWidget(self.lineEdit)

        self.hbox = QtGui.QHBoxLayout()
        self.btnOK = QtGui.QPushButton("&OK")
        self.btnCancel = QtGui.QPushButton("&Cancel")
        self.btnCancel.setDefault(True)
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)


def on_accepted():
    print("on_accepted")


def on_rejected():
    print("on_rejected")


def on_finished(status):
    print("on_finished", status)


def on_clicked():
    dialog = MyDialog(window)
    dialog.accepted.connect(on_accepted)
    dialog.rejected.connect(on_rejected)
    dialog.finished["int"].connect(on_finished)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.lineEdit.text())
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>",
              result)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())