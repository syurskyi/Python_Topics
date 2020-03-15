# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Скрыть плавающее меню")
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
        self.menuFile.setTearOffEnabled(True)

        self.actOpen = QtGui.QAction("Open", self)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuFile.addSeparator()
        self.actExit = QtGui.QAction("Exit", self)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)
        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

        self.menuHelp = QtGui.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", self)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)

        self.menuFile.insertMenu(self.actOpen, self.menuHelp)
        self.menuNew = self.menuFile.addMenu("&Вложеное меню")
        self.menuNew.addAction("Пункт &1")

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_clicked(self):
        if self.menuFile.isTearOffMenuVisible():
            self.menuFile.hideTearOffMenu()


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())