# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


def on_clicked():
    window.move(-window.width() * 2, 0)
    QtCore.QTimer.singleShot(1000, on_timeout)


def on_timeout():
    desktop = QtGui.QApplication.desktop()
    rect1 = window.geometry()
    rect2 = window.frameGeometry()
    sw = 0 - window.x() - ((rect2.width() - rect1.width()) // 2)
    sh = 0 - window.y() - rect1.top() - window.y()
    QtGui.QPixmap.grabWindow(window.winId(),
                             sw, sh,
                             desktop.width(), desktop.height()
                             ).save("screen.png", "PNG")
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