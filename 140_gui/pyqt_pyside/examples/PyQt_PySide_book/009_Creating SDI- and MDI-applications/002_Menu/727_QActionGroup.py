# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Вывести текст установленного пункта")
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
        self.add_tool_bar()
        self.statusBar().showMessage("")

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")

        self.actOpen = QtGui.QAction(self)
        self.actOpen.setText("&Open")
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)

        self.menuFile.addSeparator()

        self.actGroup = QtGui.QActionGroup(self)
        self.actGroup.hovered["QAction *"].connect(self.on_hovered)
        self.actGroup.selected["QAction *"].connect(self.on_selected)
        self.actGroup.triggered["QAction *"].connect(self.on_triggered)

        ico = self.style().standardIcon(
            QtGui.QStyle.SP_MessageBoxCritical)

        self.actRed = QtGui.QAction("Красный", self.actGroup)
        self.actRed.setCheckable(True)
        self.actRed.setIconVisibleInMenu(False)
        self.actRed.setIcon(ico)
        self.menuFile.addAction(self.actRed)

        self.actBlue = QtGui.QAction("Синий", self.actGroup)
        self.actBlue.setCheckable(True)
        self.actBlue.setIconVisibleInMenu(False)
        self.actBlue.setIcon(ico)
        self.menuFile.addAction(self.actBlue)

        self.actGreen = QtGui.QAction("Зеленый", self.actGroup)
        self.actGreen.setCheckable(True)
        self.actGreen.setIconVisibleInMenu(False)
        self.actGreen.setIcon(ico)
        self.menuFile.addAction(self.actGreen)

        """self.actGroup = QtGui.QActionGroup(self)
        self.actGroup.addAction(self.actRed)
        self.actGroup.addAction(self.actBlue)
        self.actGroup.addAction(self.actGreen)"""

        """self.actGroup = QtGui.QActionGroup(self)
        self.actRed.setActionGroup(self.actGroup)
        self.actBlue.setActionGroup(self.actGroup)
        self.actGreen.setActionGroup(self.actGroup)"""
        self.actRed.setChecked(True)

        self.menuFile.addSeparator()

        self.actExit = QtGui.QAction("&Exit", self)
        self.actExit.setIcon(ico)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)

        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actRed)
        self.toolBar.addAction(self.actBlue)
        self.toolBar.addAction(self.actGreen)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_hovered(self, act):
        print("on_hovered", act.text())

    def on_selected(self, act):
        print("on_selected", act.text())

    def on_triggered(self, act):
        print("on_triggered", act.text())

    def on_clicked(self):
        act = self.actGroup.checkedAction()
        if act:
            print(act.text())


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QActionGroup")
window.resize(500, 350)
window.show()
sys.exit(app.exec_())