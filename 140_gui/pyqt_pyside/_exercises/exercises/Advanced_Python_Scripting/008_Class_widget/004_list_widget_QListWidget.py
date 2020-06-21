from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
path = os.path.dirname(__file__)
# pa__ = 'C:/Users/serge/Dropbox/nuke/.nuke/GIZMOS/Filter/'  # peremenaja s kotoroj dostajytsja fajlu

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.list = QListWidget()         # dlja dobavlenije elementov v QListWidget y nas est' 3 fynkcii
                                            # addItem prinimaet string, toest' label
                                            # addItem 2oj variant QListWidgetItem - specialnuj klas otvechajychij za elementu spiska.
                                            # addItems QStringList, spisok strok, v Python eto obuchnuj spisov v kotorom mu podajom stroki
        ly.addWidget(self.list)
        self.textBrowser = QTextBrowser()
        ly.addWidget(self.textBrowser)

        # connect
        self.list.itemClicked.connect(self.updateText)   # itemClicked vozvrachaet vudelenuj element
        # list.itemDoubleClicked.connect(____.openFile)

        # start
        self.resize(500, 400)
        self.fillList()
        # print fullPath('t')

    def fullPath(self, item):
        # print __.pa__.j..(pa__, item.t..
        return os.path.join(path, item.text())


    def fillList(self):
        # ____.list.addItem('ITEM')
        for f in os.listdir(path):
            self.list.addItem(f)
            print(f)

    def updateText(self, item):                          # fynkcija kotoraja srabatuvaet po signaly  ____.list.itemClicked.connect(____.updateText)
        print(item)
        print(item.text())                               # tekst s itema mozno zsbrat' s pomochjy metoda text(), kotoruj vozvrachaet string
        text = open(self.fullPath(item)).read()
        print(type(text))
        self.textBrowser.setText(text)
    #
    # ___ openFile(____, item):
    #     pa__ = ____.fullPath(item)
    #     # print pa__
    #     __.system(pa__)


if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()
