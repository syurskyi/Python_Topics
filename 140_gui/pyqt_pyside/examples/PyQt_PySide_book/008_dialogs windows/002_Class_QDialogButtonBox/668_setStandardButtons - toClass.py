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

        self.box = QtGui.QDialogButtonBox()
        self.box.setOrientation(QtCore.Qt.Horizontal)
        self.box.setCenterButtons(True)
        self.box.setStandardButtons(QtGui.QDialogButtonBox.Ok |
                                    QtGui.QDialogButtonBox.Cancel |
                                    QtGui.QDialogButtonBox.Help)
        self.box.accepted.connect(self.accept)
        self.box.rejected.connect(self.reject)
        self.box.helpRequested.connect(self.on_help_requested)
        self.box.clicked["QAbstractButton *"].connect(
            self.on_btn_clicked)

        self.mainBox.addWidget(self.box)

        self.setLayout(self.mainBox)

    def on_help_requested(self):
        print("Нажата кнопка с ролью HelpRole")

    def on_btn_clicked(self, btn):
        if btn:
            print("Нажата кнопка", btn.text())


def on_clicked():
    dialog = MyDialog(window)
    dialog.box.button(QtGui.QDialogButtonBox.Cancel).setDefault(True)
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