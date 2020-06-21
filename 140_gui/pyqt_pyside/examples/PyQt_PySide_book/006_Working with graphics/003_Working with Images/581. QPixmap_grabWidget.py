# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.pix = QtGui.QPixmap("foto.jpg", "JPG")

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)


def on_clicked():
    QtGui.QPixmap.grabWidget(widget).save("widget.png", "PNG")


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    window.setWindowTitle("Класс QPixmap")
    window.move(0, 0)
    box = QtGui.QVBoxLayout()
    widget = MyWindow()
    button = QtGui.QPushButton("Сделать скриншот")
    button.clicked.connect(on_clicked)
    box.addWidget(widget)
    box.addWidget(button)
    window.setLayout(box)
    window.show()
    sys.exit(app.exec_())