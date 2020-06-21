from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("insertRow")
        self.resize(300, 150)

        lineEdit = QtGui.QLineEdit()
        textEdit = QtGui.QTextEdit()
        button1 = QtGui.QPushButton("О&тправить")
        button2 = QtGui.QPushButton("О&чистить")

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        form = QtGui.QFormLayout()

        form.insertRow(0, "&Описание:", textEdit)
        form.insertRow(0, "&Название:", lineEdit)
        form.insertRow(-1, hbox)

        self.setLayout(form)

