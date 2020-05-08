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
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files = []                            # eto peremenaja sozdajotsja dlja izbezanija sozdanija dyblikatov

    def dropEvent(self, event):
        # print 'DROP', type(event)
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())       # KOgda mu polychaem pyt' mu vuzuvaem fynkcijy addFile()

    def dragEnterEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            event.accept()
        else:
            event.ignore()

    def startDrag(self, dropAction):
        drag = QDrag(self)
        mimedata = QMimeData()
        url = []
        for i in self.selectedItems():
            url.append(i.data(Qt.UserRole))
        print(url)

    def addFile(self, path):                              # fynkcija kotoraja prinimaet pyt', pyt' mu polychaem s Drop Event
        if not path in self.files:                        # hranitsja byfer yze dobavlennuh fajlov
            item = QListWidgetItem(self)                  # mu sozdajom novuj Item
            item.setText(os.path.basename(path))          # otpravljaem imja fajla
            item.setData(Qt.UserRole, path)               # polnuj pyt' fajla polozim v kastomnujy daty etogo fajla
            self.files.append(path)

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()