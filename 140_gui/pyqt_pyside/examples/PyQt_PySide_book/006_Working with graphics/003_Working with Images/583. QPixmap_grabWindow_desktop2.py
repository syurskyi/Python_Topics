# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


def on_clicked():
    window.move(-window.width() * 2, 0)
    QtCore.QTimer.singleShot(1000, on_timeout)


def on_timeout():
    desktop = QtGui.QApplication.desktop()
    QtGui.QPixmap.grabWindow(desktop.screen().winId()).save("screen.png", "PNG")
    window.move(0, 0)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    window.setWindowTitle("Класс QPixmap")
    window.move(0, 0)
    box = QtGui.QVBoxLayout()
    button = QtGui.QPushButton("Сделать скриншот экрана")
    button.clicked.connect(on_clicked)
    box.addWidget(button)
    window.setLayout(box)
    window.show()
    sys.exit(app.exec_())