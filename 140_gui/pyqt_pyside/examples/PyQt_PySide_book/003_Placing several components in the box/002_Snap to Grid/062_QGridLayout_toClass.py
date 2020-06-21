from PyQt5 import QtWidgets
import sys

class SampleWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Выравнивание по сетке")
        self.resize(300, 50)
        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        grid = QtWidgets.QGridLayout()
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 1, 0)
        grid.addWidget(button4, 1, 1)
        self.setLayout(grid)

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtWidgets.QApplication(sys.argv)
    main = SampleWindow()
    main.show()

    if app is not None:
        app.exec_()