# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Удалить все свойства панели 4")
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
        # self.setAnimated(False)
        self.add_menu()
        self.add_dock_widget()

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_dock_widget(self):
        self.dw = QtGui.QDockWidget("MyDockWidget1")
        self.dw.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.lbl = QtGui.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw)

        self.dw2 = QtGui.QDockWidget("MyDockWidget2")
        self.dw2.setFeatures(QtGui.QDockWidget.DockWidgetClosable |
                             QtGui.QDockWidget.DockWidgetMovable)
        self.lbl2 = QtGui.QLabel("Содержимое панели 2")
        self.lbl2.setWordWrap(True)
        self.lbl2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw2.setWidget(self.lbl2)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.dw2)

        self.dw3 = QtGui.QDockWidget("MyDockWidget3")
        self.dw3.setFeatures(QtGui.QDockWidget.DockWidgetClosable |
                             QtGui.QDockWidget.DockWidgetMovable |
                             QtGui.QDockWidget.DockWidgetFloatable)
        self.lbl3 = QtGui.QLabel("Содержимое панели 3")
        self.lbl3.setWordWrap(True)
        self.lbl3.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw3.setWidget(self.lbl3)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw3)

        self.dw4 = QtGui.QDockWidget("MyDockWidget4")
        self.dw4.setFeatures(QtGui.QDockWidget.DockWidgetClosable |
                             QtGui.QDockWidget.DockWidgetMovable |
                             QtGui.QDockWidget.DockWidgetFloatable |
                             QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.lbl4 = QtGui.QLabel("Содержимое панели 4")
        self.lbl4.setWordWrap(True)
        self.lbl4.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw4.setWidget(self.lbl4)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dw4)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        self.dw4.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QDockWidget")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())