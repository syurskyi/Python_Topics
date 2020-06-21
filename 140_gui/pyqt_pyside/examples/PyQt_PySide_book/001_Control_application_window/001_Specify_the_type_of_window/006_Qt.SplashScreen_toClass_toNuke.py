from PySide import QtGui, QtCore
import sys


class SplashScreenExamapleClass(QtGui.QWidget):


    # Constructor function
    def __init__(self):
        super(SplashScreenExamapleClass, self).__init__()
        self.setWindowFlags(QtCore.Qt.SplashScreen)
        self.setWindowTitle("Name Window")
        self.resize(300, 50)

        btn = QtGui.QPushButton("Close Window", self)
        btn.setGeometry(50, 10, 200, 30)

        QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), QtCore.QCoreApplication.instance().quit)



def main():
    global c
    c = SplashScreenExamapleClass()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2

    c.show()

main()