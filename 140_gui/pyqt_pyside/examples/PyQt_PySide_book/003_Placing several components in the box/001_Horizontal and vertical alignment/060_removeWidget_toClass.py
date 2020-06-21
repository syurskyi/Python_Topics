from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("removeWidget")
        self.resize(300, 150)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        button4 = QtGui.QPushButton("4")
        button5 = QtGui.QPushButton("5")
        button6 = QtGui.QPushButton("6")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button4)
        hbox.addWidget(button5)
        hbox.addWidget(button6)
        vbox.addLayout(hbox)

        hbox.removeWidget(button5)   # Удаление из контейнера hbox
        vbox.addWidget(button5)      # Добавление в контейнер vbox

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