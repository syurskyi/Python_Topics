from PySide import QtGui


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

def main():
    main.panel = MyWindow()
    main.panel.show()

main()