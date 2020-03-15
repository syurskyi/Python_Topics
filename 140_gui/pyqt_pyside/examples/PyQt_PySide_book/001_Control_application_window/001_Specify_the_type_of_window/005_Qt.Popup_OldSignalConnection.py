from PySide.QtGui import *
from PySide.QtCore import *



class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowFlags(Qt.Popup)
        self.setWindowTitle("Window Title")
        self.resize(300, 50)

        btn = QPushButton("Print", self)
        btn.setGeometry(50, 10, 200, 30)

        self.connect(btn, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('action()')) ### also working without QtCore. Looks bottom example

    def action(self):
        nuke.createNode('Blur')

def main():
    global c
    c = Example()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()


main()


#####################################################################################################################

from PySide.QtGui import *
from PySide.QtCore import *



class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowFlags(Qt.Popup)
        self.setWindowTitle("Window Title")
        self.resize(300, 50)

        btn = QPushButton("Print", self)
        btn.setGeometry(50, 10, 200, 30)

        self.connect(btn, SIGNAL('clicked()'), self, SLOT('action()'))

    def action(self):
        nuke.createNode('Blur')

def main():
    global c
    c = Example()
    desktop = QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()


main()
