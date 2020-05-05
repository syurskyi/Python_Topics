from PySide import QtCore, QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowTitle("Выравнивание по сетке")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button4 = QtGui.QPushButton("4")
        grid = QtGui.QGridLayout()
        grid.addWidget(button1, 0, 0, 2, 1)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button4, 1, 1)
        self.setLayout(grid)
        self.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()

    if app is not None:
        app.exec_()