# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.unit_ui()

    def unit_ui(self):

        self.setWindowTitle("Display the window in the center of the screen")
        self.resize(300, 100)
        self.center()

        self.show()

    def center(self):
        desktop = QtGui.QApplication.desktop()
        self.move(desktop.availableGeometry().center() -
                    self.rect().center())



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


