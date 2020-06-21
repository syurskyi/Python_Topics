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
        self.btnCancel.clicked.connect(self.hide)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)


def on_clicked():
    if not dialog.isVisible():
        dialog.lineEdit.setText("")
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()


def on_accept():
    dialog.hide()
    print(dialog.lineEdit.text())


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

window2 = QtGui.QWidget()
window2.setWindowTitle("Это окно не будет блокировано при WindowModal")
window2.resize(500, 100)
window2.show()

dialog = MyDialog(window)
dialog.setModal(True)
dialog.btnOK.clicked.connect(on_accept)
dialog.hide()

sys.exit(app.exec_())