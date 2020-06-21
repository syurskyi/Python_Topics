# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Сделать меню недоступным")
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.add_menu()

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")

        self.menuFile.hovered["QAction *"].connect(self.on_hovered)
        self.menuFile.triggered["QAction *"].connect(self.on_triggered)
        self.menuFile.aboutToShow.connect(self.on_aboutToShow)
        self.menuFile.aboutToHide.connect(self.on_aboutToHide)

        self.actOpen = QtGui.QAction("Open", self)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)

        self.actExit = QtGui.QAction("Exit", None)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)
        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_hovered(self, act):
        print("on_hovered", act.text())

    def on_triggered(self, act):
        print("on_triggered", act.text())

    def on_aboutToShow(self):
        print("on_aboutToShow")

    def on_aboutToHide(self):
        print("on_aboutToHide")

    def on_clicked(self):
        self.menuFile.menuAction().setEnabled(False)
        self.w.button.setEnabled(False)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())