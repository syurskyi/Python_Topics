

def on_clicked():
    tab.setCurrentWidget(label2)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QTabWidget")
        self.resize(400, 150)
        tab = QtGui.QTabWidget()
        button = QtGui.QPushButton("Сделать вкладку 2 видимой")
        button.clicked.connect(on_clicked)
        label1 = QtGui.QLabel("Содержимое вкладки 1")
        label2 = QtGui.QLabel("Содержимое вкладки 2")
        tab.addTab(label1, "Вкладка &1")
        tab.addTab(label2, "Вкладка &2")
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        vbox.addWidget(button)
        self.setLayout(vbox)
