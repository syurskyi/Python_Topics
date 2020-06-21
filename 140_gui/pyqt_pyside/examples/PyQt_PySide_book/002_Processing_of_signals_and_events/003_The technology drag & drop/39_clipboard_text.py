# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.lineEdit = QtWidgets.QLineEdit()
        self.btnСut = QtWidgets.QPushButton("Вырезать")
        self.btnPaste = QtWidgets.QPushButton("Вставить")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.btnСut)
        self.vbox.addWidget(self.btnPaste)
        self.setLayout(self.vbox)
        self.btnСut.clicked.connect(self.on_cut)
        self.btnPaste.clicked.connect(self.on_paste)
        QtWidgets.qApp.clipboard().dataChanged.connect(
                     self.on_change_clipboard)

    def on_cut(self):
        text = self.lineEdit.text()
        if len(text) != 0:
            QtWidgets.qApp.clipboard().setText(text)
            self.lineEdit.setText("")

    def on_paste(self):
        text = QtWidgets.qApp.clipboard().text()
        if len(text) > 0:
            self.lineEdit.setText(text)

    def on_change_clipboard(self):
        print("Данные в буфере обмена изменены")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Работа с буфером обмена")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())