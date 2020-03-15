# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Кнопка")
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
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QtCore.QSize(32, 32))
        # self.setAnimated(False)
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks |
                            QtGui.QMainWindow.AllowTabbedDocks)
        self.setTabPosition(QtCore.Qt.LeftDockWidgetArea,
                            QtGui.QTabWidget.North)
        self.setTabPosition(QtCore.Qt.RightDockWidgetArea,
                            QtGui.QTabWidget.North)
        self.setTabShape(QtGui.QTabWidget.Triangular)
        self.add_menu()
        self.add_tool_bar()
        self.add_dock_widget()
        self.statusBar().showMessage("Текст в строке состояния")

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_MessageBoxCritical)
        self.actClose = self.toolBar.addAction(ico, "Close",
                                               QtGui.qApp.quit)
        self.actClose.setShortcut(QtGui.QKeySequence.Close)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # self.addToolBarBreak(QtCore.Qt.TopToolBarArea)
        self.toolBar2 = QtGui.QToolBar("MyToolBar2")
        ico2 = self.style().standardIcon(
            QtGui.QStyle.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico2, "Quit",
                                               QtGui.qApp.quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.Quit)
        # self.insertToolBar(self.toolBar, self.toolBar2)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar2)
        # self.insertToolBarBreak(self.toolBar2)

    def add_dock_widget(self):
        self.dw = QtGui.QDockWidget("MyDockWidget1")
        self.lbl = QtGui.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw)

        self.dw2 = QtGui.QDockWidget("MyDockWidget2")
        self.lbl2 = QtGui.QLabel("Содержимое панели 2")
        self.lbl2.setWordWrap(True)
        self.lbl2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw2.setWidget(self.lbl2)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw2,
                           QtCore.Qt.Vertical)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        print("Нажата кнопка")


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMainWindow")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())