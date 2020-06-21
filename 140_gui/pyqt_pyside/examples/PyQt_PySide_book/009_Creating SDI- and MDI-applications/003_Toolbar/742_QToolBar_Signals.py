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
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setFloatable(True)

        self.toolBar.actionTriggered["QAction *"].connect(
            self.on_triggered)
        self.toolBar.topLevelChanged["bool"].connect(
            self.on_topLevelChanged)
        self.toolBar.visibilityChanged["bool"].connect(
            self.on_visibilityChanged)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.addToolBarBreak(QtCore.Qt.TopToolBarArea)

        self.toolBar2 = QtGui.QToolBar("MyToolBar2")
        self.toolBar2.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar2.setFloatable(False)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico, "Quit",
                                               QtGui.qApp.quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.Quit)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar2)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_triggered(self, act):
        print("Выбрано дейстие", act.text())

    def on_topLevelChanged(self, status):
        print("on_topLevelChanged", status)

    def on_visibilityChanged(self, status):
        print("visibilityChanged", status)

    def on_clicked(self):
        print(self.toolBar.isFloating())


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())