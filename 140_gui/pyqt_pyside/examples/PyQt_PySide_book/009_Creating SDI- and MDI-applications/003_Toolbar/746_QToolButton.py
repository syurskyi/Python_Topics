# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Проверить положение панели")
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
        self.setIconSize(QtCore.QSize(32, 32))
        # self.setAnimated(False)
        self.add_menu()
        self.add_tool_bar()

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_ComputerIcon)
        self.actOpen.setIcon(ico)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actOpen)
        self.toolBtn1 = self.toolBar.widgetForAction(self.actOpen)
        self.toolBtn1.setAutoRaise(False)

        self.actQuit = QtGui.QAction("Quit", None)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_DialogCloseButton)
        self.actQuit.setIcon(ico)
        self.actQuit.setToolTip("Выход из приложения")
        self.actQuit.triggered.connect(self.on_quit)

        self.menuHelp = QtGui.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", None)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)

        self.toolBtn2 = QtGui.QToolButton()
        self.toolBtn2.setDefaultAction(self.actQuit)
        self.toolBtn2.setMenu(self.menuHelp)
        # self.toolBtn2.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolBtn2.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        # self.toolBtn2.setPopupMode(QtGui.QToolButton.InstantPopup)
        # self.toolBtn2.setArrowType(QtCore.Qt.DownArrow)
        self.toolBtn2.triggered["QAction *"].connect(self.on_triggered)

        self.toolBar.addWidget(self.toolBtn2)

        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_quit(self):
        print("Нажата кнопка Quit")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_triggered(self, act):
        print("Выбрано дейстие", act.text())

    def on_clicked(self):
        print(self.toolBar.isFloating())


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolButton")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())