
def on_clicked():
    splitter.insertWidget(0, label3)
    button.setEnabled(False)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QSplitter")
        self.resize(300, 350)
        button = QtGui.QPushButton("Добавить компонент")
        button.clicked.connect(on_clicked)
        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        label1 = QtGui.QLabel("Содержимое компонента 1")
        label2 = QtGui.QLabel("Содержимое компонента 2")
        label3 = QtGui.QLabel("Содержимое компонента 3")
        label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        label3.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        splitter.addWidget(label1)
        splitter.addWidget(label2)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(splitter)
        vbox.addWidget(button)
        self.setLayout(vbox)
