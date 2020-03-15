# -*- coding: utf-8 -*-
from PyQt4 import QtGui


class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, id, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, e):
        print("Receive focus field", self.id)
        QtGui.QLineEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        print("Lost focus field", self.id)
        QtGui.QLineEdit.focusOutEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)
        self.button = QtGui.QPushButton("Receive focus field 2")
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)
        # Задаем порядок обхода с помощью клавиши <Tab>
        QtGui.QWidget.setTabOrder(self.line1, self.line2)
        QtGui.QWidget.setTabOrder(self.line2, self.button)

    def on_clicked(self):
        self.line2.setFocus()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())