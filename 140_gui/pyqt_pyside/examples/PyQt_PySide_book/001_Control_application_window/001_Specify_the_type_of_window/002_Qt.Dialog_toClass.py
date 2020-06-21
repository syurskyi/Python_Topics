# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import sys


class SampleWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.unit_ui()

    def unit_ui(self):
        btn = QtWidgets.QPushButton("Close Window", self)
        btn.setGeometry(50, 10, 200, 30)
        # QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), app.quit)  # This old style
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowTitle("Name Window")
        self.resize(300, 50)
        self.center()

        self.show()

    def center(self):
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

# this is for Nuke

# if __name__ == '__main__':
#     import sys
#
#     app = None
#     try:
#         import nuke
#     except ImportError:
#         app = QtGui.QApplication(sys.argv)
#     main = SampleWindow()
#     main.show()
#
#     if app is not None:
#         app.exec_()

# this is only for PyCharm

def main():
    app = None

    app = QtWidgets.QApplication(sys.argv)
    ex = SampleWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
