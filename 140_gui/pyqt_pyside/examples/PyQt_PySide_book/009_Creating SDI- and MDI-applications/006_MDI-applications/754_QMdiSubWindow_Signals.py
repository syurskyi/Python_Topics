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
        self.n = 1
        self.mdi_area = QtGui.QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.add_menu()

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.actCreate = QtGui.QAction("&Создать окно", None)
        self.actCreate.triggered.connect(self.on_create_sub_window)
        self.menuFile.addAction(self.actCreate)

        self.menuBar().addMenu(self.menuFile)

        self.menuWindow = QtGui.QMenu("&Window")
        self.actNext = QtGui.QAction("&Next", None)
        self.actNext.triggered.connect(
            self.mdi_area.activateNextSubWindow)
        self.menuWindow.addAction(self.actNext)

        self.actCloseActive = QtGui.QAction("CloseActi&ve", None)
        self.actCloseActive.triggered.connect(
            self.mdi_area.closeActiveSubWindow)
        self.menuWindow.addAction(self.actCloseActive)

        self.actCloseAll = QtGui.QAction("Close&All", None)
        self.actCloseAll.triggered.connect(
            self.mdi_area.closeAllSubWindows)
        self.menuWindow.addAction(self.actCloseAll)

        self.menuBar().addMenu(self.menuWindow)

    def on_create_sub_window(self):
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_ComputerIcon)
        w = MyWidget()
        sWindow = self.mdi_area.addSubWindow(w)
        sWindow.aboutToActivate.connect(self.on_aboutToActivate)
        sWindow.windowStateChanged["Qt::WindowStates", "Qt::WindowStates"].connect(
            self.on_windowStateChanged)
        sWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        sWindow.resize(300, 150)
        sWindow.setWindowIcon(ico)
        sWindow.setWindowTitle("Вложенное окно {0}".format(self.n))
        self.n += 1
        sWindow.show()

    def on_aboutToActivate(self):
        print("on_aboutToActivate")

    def on_windowStateChanged(self, s1, s2):
        print("on_windowStateChanged", s1, s2)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMdiSubWindow")
window.resize(700, 350)
window.show()
sys.exit(app.exec_())