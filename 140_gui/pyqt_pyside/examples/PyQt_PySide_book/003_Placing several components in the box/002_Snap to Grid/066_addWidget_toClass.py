from PySide import QtCore, QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowTitle("Выравнивание по сетке")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        grid = QtGui.QGridLayout()
        grid.addWidget(button1, 0, 0, alignment=QtCore.Qt.AlignLeft)
        grid.addWidget(button2, 0, 1, QtCore.Qt.AlignRight)
        grid.addWidget(button3, 1, 0, 1, 2)
        self.setLayout(grid)

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