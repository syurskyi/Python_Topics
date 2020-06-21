from PySide import QtGui, QtCore
import sys


class SampleWindow(QtGui.QWidget):
    """ Our main window class
    """

    # Constructor function
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint) #  Gives the window a thin dialog border on Windows.
        self.setWindowTitle("Name Window")
        self.resize(300, 70)

        btn = QtGui.QPushButton("Close Window", self)
        btn.setGeometry(50, 10, 200, 30)

        # QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), QtCore.QCoreApplication.instance().quit)



def main():
    global c
    c = SampleWindow()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()