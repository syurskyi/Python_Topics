# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.unit_ui()

    def unit_ui(self):
        self.setWindowFlags(QtCore.Qt.Window |
                              QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Window title")
        self.resize(300, 70)

        self.center()
        self.set_button()

        self.show()

    def center(self):
        desktop = QtGui.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

    def set_button(self):
        btn = QtGui.QPushButton("Close window", self)
        btn.setGeometry(50, 10, 200, 30)
        # QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), app.quit)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)


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

    app = QtGui.QApplication(sys.argv)
    ex = SampleWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

