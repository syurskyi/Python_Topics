from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class windowClass(QMainWindow):
    def __init__(self):
        super(windowClass, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)  # etot metod est' tol'ko y QMainWindow

        self.menuBar = QMenuBar()      # shto bu programno sozdat' menubar ili statusbar, nyzno snachalo sozdat'
                                       # etot widget kak objekt
        self.setMenuBar(self.menuBar)

        self.menu = QMenu('File')
        self.menuBar.addMenu(self.menu)

        self.act1 = QAction('Open', self)
        self.menu.addAction(self.act1)


if __name__ == '__main__':
    app = QApplication([])
    w = windowClass()
    w.show()
    app.exec_()