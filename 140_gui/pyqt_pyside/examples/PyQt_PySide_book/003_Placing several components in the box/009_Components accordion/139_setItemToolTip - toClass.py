from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QToolBox")
        self.resize(300, 250)
        toolBox = QtGui.QToolBox()
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        toolBox.setItemToolTip(0, "Это текст подсказки для вкладки 1")
        toolBox.setItemToolTip(1, "Это текст подсказки для вкладки 2")
        toolBox.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(toolBox)
        self.setLayout(vbox)
