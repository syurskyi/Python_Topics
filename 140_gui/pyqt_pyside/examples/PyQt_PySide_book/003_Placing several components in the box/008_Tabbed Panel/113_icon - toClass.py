from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QTabWidget")
        self.resize(400, 120)
        tab = QtGui.QTabWidget()
        style = self.style()
        icon1 = style.standardIcon(QtGui.QStyle.SP_DriveHDIcon)
        icon2 = style.standardIcon(QtGui.QStyle.SP_DriveCDIcon)
        icon3 = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
        tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), icon1, "Вкладка &1")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), icon2, "Вкладка &2")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 3"), icon3, "Вкладка &3")
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
