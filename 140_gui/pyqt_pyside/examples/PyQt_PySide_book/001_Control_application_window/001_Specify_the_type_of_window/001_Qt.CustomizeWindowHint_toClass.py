from PyQt5 import QtCore, QtWidgets
import sys


class SampleWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowTitle("Customize Window Hint")
        self.resize(300, 70)
        self.setWindowFlags(QtCore.Qt.Window |
                              QtCore.Qt.CustomizeWindowHint)
        btn = QtWidgets.QPushButton("Close window", self)
        btn.setGeometry(50, 10, 200, 30)
        QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), app.quit)
        # desktop = QtGui.QApplication.desktop()
        # x = (desktop.width() - self.width()) // 2
        # y = (desktop.height() - self.height()) // 2
        # self.move(x, y)

def main():

    # app = QtGui.QApplication(sys.argv)
    global window
    window = SampleWindow()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    # sys.exit(app.exec_())

main()