# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.lineEdit = QtGui.QLineEdit()
        self.btnСut = QtGui.QPushButton("Cut")
        self.btnPaste = QtGui.QPushButton("Paste")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.btnСut)
        self.vbox.addWidget(self.btnPaste)
        self.setLayout(self.vbox)
        self.btnСut.clicked.connect(self.on_cut)
        self.btnPaste.clicked.connect(self.on_paste)
        self.connect(QtGui.qApp.clipboard(), QtCore.SIGNAL("dataChanged()"),
                     self.on_change_clipboard)

    def on_cut(self):
        text = self.lineEdit.text()
        if len(text) != 0:
            QtGui.qApp.clipboard().setText(text)
            self.lineEdit.setText("")

    def on_paste(self):
        text = QtGui.qApp.clipboard().text()
        if len(text) > 0:
            self.lineEdit.setText(text)

    def on_change_clipboard(self):
        print("Data in the clipboard changed")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Working with the clipboard")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())