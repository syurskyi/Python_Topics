from PySide import QtGui, QtCore
import sys


class ToolExampleClass(QtGui.QWidget):


    # Constructor function
    def __init__(self):
        super(ToolExampleClass, self).__init__()
        self.setWindowFlags(QtCore.Qt.ToolTip)
        self.setWindowTitle("Name Window")
        self.resize(300, 50)

        # self.btn = QtGui.QPushButton("Close Window", self)
        # self.btn.setGeometry(50, 10, 200, 30)

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        self.btn = QtGui.QPushButton('Close Window', self)
        layout.addWidget(self.btn)

        self.btn.clicked.connect(self.action)


    def action(self):
        self.btn.setText('Presseed')
        self.btn.clicked.connect(self.close)


def main():
    global c
    c = ToolExampleClass()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()

main()