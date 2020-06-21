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

        self.box = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        self.btnOK = self.box.addButton("&OK",
                                        QtGui.QDialogButtonBox.AcceptRole)
        self.btnCancel = self.box.addButton("&Cancel",
                                            QtGui.QDialogButtonBox.RejectRole)
        self.box.accepted.connect(self.accept)
        self.box.rejected.connect(self.reject)

        self.mainBox.addWidget(self.box)

        self.setLayout(self.mainBox)


def on_clicked():
    dialog = MyDialog(window)
    dialog.btnCancel.setDefault(True)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.lineEdit.text())
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>",
              result)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QDialogButtonBox")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())