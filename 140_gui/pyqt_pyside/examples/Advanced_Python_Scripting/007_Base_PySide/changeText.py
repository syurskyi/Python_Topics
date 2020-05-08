from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from import PyQt4 import QtCore


class SimpleWindowClass(QWidget):
    def __init__(self):
        super(SimpleWindowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel('Text')
        layout.addWidget(self.label)
        self.button = QPushButton('Press')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action)

    def action(self):
        self.label.setText('New Text')
        self.button.setText('Presseed')
        self.button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication([])
    w = SimpleWindowClass()
    w.show()
    app.exec_()
