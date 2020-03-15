# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setCursor(QtGui.QCursor(QtGui.QPixmap("Cursor.png"), 0, 0))
        self.label = QtGui.QLabel("Click in the window")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    def mousePressEvent(self, e):
        self.label.setText("X: {0}, Y: {1}".format(e.x(), e.y()))
        e.ignore()
        QtGui.QWidget.mousePressEvent(self, e)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Custom Cursor")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())