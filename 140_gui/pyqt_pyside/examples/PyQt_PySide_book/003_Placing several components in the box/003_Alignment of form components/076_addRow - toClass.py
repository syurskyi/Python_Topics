from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("addRow")
        self.resize(300, 150)

        label1 = QtGui.QLabel("&Название:")
        label2 = QtGui.QLabel("&Описание:")
        lineEdit = QtGui.QLineEdit()
        textEdit = QtGui.QTextEdit()
        button1 = QtGui.QPushButton("О&тправить")
        button2 = QtGui.QPushButton("О&чистить")

        label1.setBuddy(lineEdit)
        label2.setBuddy(textEdit)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        form = QtGui.QFormLayout()
        form.addRow(label1, lineEdit)
        form.addRow(label2, textEdit)
        form.addRow(hbox)
        self.setLayout(form)

