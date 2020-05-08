from PySide2.QtGui import *
from PySide2.QtWidgets import *
import dialog

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        self.dial = dialog.dialogClass()
        r = self.dial.exec_()
        print(r)
        if r:
            print(self.dial.getData())
            # print self.dial.label.text()

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()

# Sam klass QDialog ynasledovan ot klassa Widgeta.
# A znachit y nego est'  metod show. No on y nas prosto otkroet okno.
# To est'  programma prodolzet dal'she dejstvovat', kak esli bu mu otkruli dochernee okno.
# Shtobu dialog zarabotal kak dialog y nas est' fynkcija exec. No shto bu eta fynkcija sto to vernyla
# dlja etogo est' 2 specialnue fynkcii, kotorue nyzno vuzvat'. Eto accept i rejcet. Mu na nih
# dolznu zakonektit' nashi knopki
#
# KOgda y nas dialog i tam mnogo kakih to parametrov, nyzno sdelat'  kakyjy to fynkcijy, kotoraja iz etih parametrov
# nam soberjot ydobnuj naprimer slovar'.