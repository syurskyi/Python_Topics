# -*- coding: utf-8 -*-
from PyQt4 import QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def closeEvent(self, e):
        result = QtGui.QMessageBox.question(self,
                       "Confirm Window Closure",
                       "Are you sure you want to close the window?",
                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                       QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            e.accept()
            QtGui.QWidget.closeEvent(self, e)
        else:
            e.ignore()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())