from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("WrapLongRows")
        self.resize(300, 150)
        lineEdit = QtGui.QLineEdit()
        textEdit = QtGui.QTextEdit()
        button1 = QtGui.QPushButton("О&тправить")
        button2 = QtGui.QPushButton("О&чистить")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        form = QtGui.QFormLayout()
        form.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        form.addRow("&Название литературного или другого произведения:", lineEdit)
        form.addRow("&Описание:", textEdit)
        form.addRow(hbox)
        self.setLayout(form)
