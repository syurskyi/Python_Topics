import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)

    def dropEvent(self, event):
        print('DROP', type(event))
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            print(mimedata.urls())
        elif mimedata.hasColor():
            print(mimedata.colorData())
        elif mimedata.hasText():
            print(mimedata.text())


    def dragEnterEvent(self, event):
        event.accept()
        print('ENTER', type(event))

    def dragMoveEvent(self, event):
        event.accept()
        # print 'MOVE'


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = listWidgetClass()
    main.show()

    if app is not None:
        app.exec_()