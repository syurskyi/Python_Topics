# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyLabel(QtGui.QLabel):
    def __init__(self, txt, parent=None):
        QtGui.QLabel.__init__(self, txt, parent)

    def event(self, e):
        if e.type() == QtCore.QEvent.StatusTip:
            self.setText(e.tip())
            return True
        return QtGui.QLabel.event(self, e)


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Сделать доступным/недоступным")
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
        self.actOpen.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actOpen.setToolTip("Текст всплывающей подсказки")
        self.actOpen.setWhatsThis("Текст справки")
        self.actOpen.setStatusTip("Текст для строки состояния")
        self.actOpen.triggered.connect(self.on_open)
        self.actOpen.hovered.connect(self.on_hovered)
        self.menuFile.addAction(self.actOpen)

        self.actCheckable = QtGui.QAction("&Checkable", self)
        self.actCheckable.setCheckable(True)
        self.actCheckable.setChecked(True)
        self.actCheckable.setIconVisibleInMenu(False)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_MessageBoxCritical)
        self.actCheckable.setIcon(ico)
        f = self.actCheckable.font()
        f.setBold(True)
        self.actCheckable.setFont(f)
        self.actCheckable.changed.connect(self.on_changed)
        self.actCheckable.toggled["bool"].connect(self.on_toggled)
        self.menuFile.addAction(self.actCheckable)

        self.actSep = QtGui.QAction(self)
        self.actSep.setSeparator(True)
        self.menuFile.addAction(self.actSep)

        self.actExit = QtGui.QAction("&Exit", self)
        self.actExit.setIcon(ico)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)

        self.actH = QtGui.QAction("H&elps", self)
        ico2 = self.style().standardIcon(
            QtGui.QStyle.SP_MessageBoxInformation)
        self.actH.setIcon(ico2)
        self.menuHelp = QtGui.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", self)
        self.actHelp.setShortcut("F1")
        self.menuHelp.addAction(self.actHelp)
        self.actH.setMenu(self.menuHelp)
        self.menuFile.addAction(self.actH)

        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actCheckable)
        self.toolBar.addAction(self.actH)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_hovered(self):
        self.actOpen.showStatusText(self.w.label)

    def on_toggled(self, status):
        print("on_toggled", status)

    def on_changed(self):
        print("on_changed")

    def on_clicked(self):
        self.actCheckable.setEnabled(not self.actCheckable.isEnabled())


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QAction")
window.resize(500, 350)
window.show()
sys.exit(app.exec_())