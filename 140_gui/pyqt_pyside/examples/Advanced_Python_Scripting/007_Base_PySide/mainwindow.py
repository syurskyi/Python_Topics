from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class WindowClass(QMainWindow):
    def __init__(self):
        super(WindowClass, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)

        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)

        self.menu = QMenu('File')
        self.menuBar.addMenu(self.menu)

        self.act1 = QAction('Open', self)
        self.menu.addAction(self.act1)


if __name__ == '__main__':
    app = QApplication([])
    w = WindowClass()
    w.show()
    app.exec_()