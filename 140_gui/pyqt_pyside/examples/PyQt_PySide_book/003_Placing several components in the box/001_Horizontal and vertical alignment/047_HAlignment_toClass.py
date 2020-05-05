from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        button5 = QtWidgets.QPushButton("5")
        button6 = QtWidgets.QPushButton("6")
        vbox = QtWidgets.QVBoxLayout()

        hbox = QtWidgets.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        vbox.addLayout(hbox)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.setContentsMargins(30, 30, 30, 30)
        hbox2.setSpacing(20)
        hbox2.addWidget(button4)
        hbox2.addWidget(button5)
        hbox2.addWidget(button6)
        vbox.addLayout(hbox2)

        self.setWindowTitle("Управление отступами")
        self.resize(400, 50)

        self.setLayout(vbox)
        self.show()

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