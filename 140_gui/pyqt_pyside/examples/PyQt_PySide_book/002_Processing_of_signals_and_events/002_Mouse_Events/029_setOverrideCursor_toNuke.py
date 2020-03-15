from PySide import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Change the mouse pointer for the application")
        self.resize(300, 70)
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.button = QtGui.QPushButton("Change mouse pointer", self)
        self.button.setGeometry(50, 10, 200, 30)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.button.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.on_timeout)

    def on_timeout(self):
        QtGui.QApplication.restoreOverrideCursor()
        self.button.setEnabled(True)


def main():
    global c
    c = MyWindow()
    c.raise_()
    c.show()

main()