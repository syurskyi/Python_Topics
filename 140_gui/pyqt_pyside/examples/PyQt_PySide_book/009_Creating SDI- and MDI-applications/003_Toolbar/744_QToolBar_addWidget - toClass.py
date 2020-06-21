# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Скрыть или отобразить список")
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
        # self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
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
        self.toolBar.addSeparator()
        self.comboBox = QtGui.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        self.comboBox.setEditable(False)
        self.comboBox.activated["const QString&"].connect(
            self.on_activated)
        self.actComboBox = self.toolBar.addWidget(self.comboBox)

        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.addToolBarBreak(QtCore.Qt.TopToolBarArea)

        self.toolBar2 = QtGui.QToolBar("MyToolBar2")
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico, "Quit",
                                               QtGui.qApp.quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.Quit)

        self.act1 = QtGui.QAction(ico, "Пункт &1", self)
        self.act2 = QtGui.QAction(ico, "Пункт &2", self)
        self.act3 = QtGui.QAction(ico, "Пункт &3", self)
        self.act4 = QtGui.QAction(ico, "Пункт &4", self)

        self.toolBar2.addActions([self.act1, self.act2,
                                  self.act3, self.act4])
        self.toolBar2.insertSeparator(self.act1)

        self.spinBox = QtGui.QSpinBox()
        self.spinBox.setRange(0, 100)
        self.spinBox.setValue(10)
        self.toolBar2.insertWidget(self.act1, self.spinBox)

        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar2)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_activated(self, s):
        print("Выбран пункт", s)

    def on_clicked(self):
        self.actComboBox.setVisible(not self.actComboBox.isVisible())


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())
