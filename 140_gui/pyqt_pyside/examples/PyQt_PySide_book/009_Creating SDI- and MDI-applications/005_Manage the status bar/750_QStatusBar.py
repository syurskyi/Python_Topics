# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.button = QtGui.QPushButton("Вывести текст в строку состояния")
        self.button2 = QtGui.QPushButton("Стереть текст в строке состояния")
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.box.addWidget(self.button2)
        self.setLayout(self.box)


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.w.button2.clicked.connect(self.statusBar().clearMessage)
        self.add_menu()
        self.label1 = QtGui.QLabel("Обычное сообщение1")
        self.label2 = QtGui.QLabel("Обычное сообщение2")
        self.label1.setMinimumSize(150, 20)
        self.label2.setMinimumSize(150, 20)
        self.label1.setFrameStyle(QtGui.QFrame.Panel |
                                  QtGui.QFrame.Sunken)
        self.label2.setFrameStyle(QtGui.QFrame.Panel |
                                  QtGui.QFrame.Sunken)
        sb = self.statusBar()
        sb.addWidget(self.label1)
        sb.addWidget(self.label2, 1)

        self.label3 = QtGui.QLabel("Постоянное сообщение1")
        self.label4 = QtGui.QLabel("Постоянное сообщение2")
        self.label3.setMinimumSize(150, 20)
        self.label4.setMinimumSize(150, 20)
        self.label3.setFrameStyle(QtGui.QFrame.Panel |
                                  QtGui.QFrame.Sunken)
        self.label4.setFrameStyle(QtGui.QFrame.Panel |
                                  QtGui.QFrame.Sunken)
        sb.addPermanentWidget(self.label3)
        sb.addPermanentWidget(self.label4)
        sb.setMinimumWidth(650)
        sb.setSizeGripEnabled(False)
        sb.messageChanged["const QString&"].connect(self.on_messageChanged)

    def add_menu(self):
        self.menuFile = QtGui.QMenu("&File")
        self.menuFile.menuAction().setStatusTip("Это описание меню File")
        self.actOpen = QtGui.QAction("&Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actOpen.setStatusTip("Это описание пункта Open")
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_messageChanged(self, s):
        print("Изменился текст в строке состояния", s)

    def on_clicked(self):
        self.statusBar().showMessage("Текст, выводимый на 2 секунды",
                                     2000)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QStatusBar")
window.resize(700, 350)
window.show()
sys.exit(app.exec_())