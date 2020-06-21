from PySide import QtGui
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Horizontal alignment in reverse order")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        hbox = QtGui.QHBoxLayout()
        hbox.setDirection(QtGui.QBoxLayout.RightToLeft)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        self.setLayout(hbox)

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