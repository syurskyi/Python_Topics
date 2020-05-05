# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setCursor(QtGui.QCursor(QtGui.QPixmap("cursor.png"), 0, 0))
        self.label = QtWidgets.QLabel("Щелкните мышью в окне")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    def mousePressEvent(self, e):
        self.label.setText("X: {0}, Y: {1}".format(e.x(), e.y()))
        e.ignore()
        QtWidgets.QWidget.mousePressEvent(self, e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Пользовательский указатель")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())