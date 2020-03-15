# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
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
        self.dw.dockLocationChanged["Qt::DockWidgetArea"].connect(
            self.on_dockLocationChanged)
        self.dw.topLevelChanged["bool"].connect(
            self.on_topLevelChanged)
        self.dw.visibilityChanged["bool"].connect(
            self.on_visibilityChanged)
        self.lbl = QtGui.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_dockLocationChanged(self, area):
        if area == QtCore.Qt.LeftDockWidgetArea:
            print("Область слева")
        elif area == QtCore.Qt.RightDockWidgetArea:
            print("Область справа")
        elif area == QtCore.Qt.TopDockWidgetArea:
            print("Область сверху")
        elif area == QtCore.Qt.BottomDockWidgetArea:
            print("Область снизу")
        else:
            print("Панель не прикреплена")

    def on_topLevelChanged(self, status):
        print("on_topLevelChanged", status)

    def on_visibilityChanged(self, status):
        print("visibilityChanged", status)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QDockWidget")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())