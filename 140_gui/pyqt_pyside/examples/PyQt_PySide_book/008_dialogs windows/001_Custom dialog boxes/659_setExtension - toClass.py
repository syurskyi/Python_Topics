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
        self.btnExt = QtGui.QPushButton("&Больше...")
        self.btnExt.setCheckable(True)
        self.btnCancel.setDefault(True)
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.btnExt.toggled["bool"].connect(self.showExtension)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.hbox.addWidget(self.btnExt)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

        self.ext = QtGui.QWidget()
        self.extBox = QtGui.QVBoxLayout()
        self.extLabel = QtGui.QLabel("Скрытый компонент")
        self.extBox.addWidget(self.extLabel)
        self.ext.setLayout(self.extBox)
        self.setExtension(self.ext)
        self.setOrientation(QtCore.Qt.Vertical)


def on_clicked():
    dialog = MyDialog(window)
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