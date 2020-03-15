from PySide.QtCore import *
from PySide.QtGui import *

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage2)

    def fillList(self):
        node = nuke.selectedNode()
        channels = node.channels()
        for f in channels:
            self.list.addItem(f)

    def showMessage2(self):
        i = QInputDialog.getItem(self, 'Enter text', 'Name:',  # Tak kak eto staticheskij metod, mu mozem vuzvat' ne sozdavaja ekzempljar klassa
                                 [str(x) for x in range(10)])
        print i


def main():
    global c
    c = simpleWindow()
    c.raise_()
    c.show()

main()