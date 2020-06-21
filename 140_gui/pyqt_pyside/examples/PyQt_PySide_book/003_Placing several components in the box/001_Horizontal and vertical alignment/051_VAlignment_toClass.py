from PyQt5 import QtCore, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Vertical alignment")
        self.resize(300, 150)
        button1 = QtWidgets.QPushButton("Bottom")
        button2 = QtWidgets.QPushButton("No")
        button3 = QtWidgets.QPushButton("Top")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(button1, alignment=QtCore.Qt.AlignBottom)
        vbox.addWidget(button2)
        vbox.addWidget(button3, alignment=QtCore.Qt.AlignTop)
        self.setLayout(vbox)


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