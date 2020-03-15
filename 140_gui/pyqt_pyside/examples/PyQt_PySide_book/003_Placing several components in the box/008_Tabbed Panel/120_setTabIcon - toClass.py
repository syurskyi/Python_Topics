

def on_clicked():
    style = window.style()
    icon = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
    tab.setTabIcon(0, icon)
    button.setEnabled(False)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QTabWidget")
        self.resize(400, 150)
        tab = QtGui.QTabWidget()
        button = QtGui.QPushButton("Установить иконку")
        button.clicked.connect(on_clicked)
        tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        vbox.addWidget(button)
        self.setLayout(vbox)
