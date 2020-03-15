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
        self.add_tool_bar()
        self.statusBar().showMessage("")

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        self.actH = QtGui.QAction("H&elps", self)
        ico2 = self.style().standardIcon(
                             QtGui.QStyle.SP_MessageBoxInformation)
        self.actH.setIcon(ico2)
        self.menuHelp = QtGui.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", self)
        self.actHelp.setShortcut("F1")
        self.menuHelp.addAction(self.actHelp)
        self.actH.setMenu(self.menuHelp)
        self.toolBar.addAction(self.actH)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)
window.show()
sys.exit(app.exec_())