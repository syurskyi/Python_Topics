import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)          # #okno bydet vsegda poverh drygih okon
        self.setDragDropMode(QAbstractItemView.DropOnly)      # shto bu dropEvent zarabotal nado vklychit dlja etogo vidgeta setDragDropMode

    def dropEvent(self, event):                # to shto proishodit kogda mu sbrasuvaem dannue na vidget
        print('DROP', type(event))
        mimedata = event.mimeData()            # kogda mu peretaskivaem element, to pomimo togo shto srabatuvaet DropEvent,
                                               # srabatuvaet echjo 2 eventa, dragEnterEvent and dragMoveEvent
                                               # obuchno oni odinakovue i govorjat mozet li nash vidget prinjat' eti dannue kotorue mu peretaskivaem
                                               # i vnytri etogo eventa kak raz proverjaetsja kakogo tipa dannue k nam prishli
                                               # i etot event dolzen skazat' mozet li nash event eti dannue prinjat'
        if mimedata.hasText():
            print('text')
        elif mimedata.hasUrls():
            print('urls')

    def dragEnterEvent(self, event):
        event.accept()
        print('ENTER', type(event))

    def dragMoveEvent(self, event):
        event.accept()
        print('MOVE')

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()