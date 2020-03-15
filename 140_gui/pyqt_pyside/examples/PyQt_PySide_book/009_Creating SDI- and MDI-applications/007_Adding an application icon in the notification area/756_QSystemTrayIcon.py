# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Отобразить сообщение в трее")
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_ComputerIcon)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.add_menu()
        self.sys_tray = QtGui.QSystemTrayIcon(ico, self)
        self.sys_tray.setToolTip("Описание приложения")
        self.on_create_context_menu()
        self.sys_tray.activated["QSystemTrayIcon::ActivationReason"].connect(self.on_activated)
        self.sys_tray.messageClicked.connect(self.on_messageClicked)
        self.sys_tray.show()

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.actExit = QtGui.QAction("&Exit", None)
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuFile.addAction(self.actExit)
        self.menuBar().addMenu(self.menuFile)

    def on_create_context_menu(self):
        self.menuSystemTray = QtGui.QMenu("&SystemTray")
        self.actShowHide = QtGui.QAction("&Отобразить или скрыть окно", None)
        self.actShowHide.triggered.connect(self.on_show_hide)
        self.menuSystemTray.addAction(self.actShowHide)

        self.menuSystemTray.addSeparator()

        self.actQuit = QtGui.QAction("&Выход", None)
        self.actQuit.triggered.connect(QtGui.qApp.quit)
        self.menuSystemTray.addAction(self.actQuit)

        self.sys_tray.setContextMenu(self.menuSystemTray)

    def closeEvent(self, e):
        self.hide()
        e.ignore()

    def on_clicked(self):
        self.sys_tray.showMessage("Название", "Текст сообщения",
                                  msecs=2000)

    def on_show_hide(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.activateWindow()

    def on_activated(self, st):
        print("on_activated", st)

    def on_messageClicked(self):
        print("on_messageClicked")


app = QtGui.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
window = MyWindow()
window.setWindowTitle("Класс QSystemTrayIcon")
window.resize(700, 350)
window.show()
sys.exit(app.exec_())