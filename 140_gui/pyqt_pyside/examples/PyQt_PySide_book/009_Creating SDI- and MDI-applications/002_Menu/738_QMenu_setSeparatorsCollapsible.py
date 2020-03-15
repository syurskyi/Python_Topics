# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Сделать меню File недоступным")
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
        self.menuFile.setSeparatorsCollapsible(False)

        self.menuFile.addSeparator()
        self.actOpen = QtGui.QAction("Open", self)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)

        self.act1 = QtGui.QAction("Пункт &1", self)
        self.act2 = QtGui.QAction("Пункт &2", self)
        self.act3 = QtGui.QAction("Пункт &3", self)
        self.act4 = QtGui.QAction("Пункт &4", self)

        self.menuFile.insertAction(self.actOpen, self.act1)
        self.menuFile.insertActions(self.actOpen, [self.act2,
                                                   self.act3, self.act4])

        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.actExit = QtGui.QAction("Exit", None)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)
        self.menuFile.addSeparator()
        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

        self.menuHelp = QtGui.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", None)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)
        self.menuBar().addMenu(self.menuHelp)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_clicked(self):
        self.menuFile.menuAction().setEnabled(False)
        self.w.button.setEnabled(False)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())