
def on_clicked():
    toolBox.setCurrentIndex(1)


from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QToolBox")
        self.resize(300, 250)
        toolBox = QtGui.QToolBox()
        button = QtGui.QPushButton("Сделать вкладку 2 видимой")
        button.clicked.connect(on_clicked)
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        toolBox.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(toolBox)
        vbox.addWidget(button)
        self.setLayout(vbox)
