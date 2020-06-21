# dialog.py
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class dialogClass(QDialog):
    def __init__(self):
        super(dialogClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.label = QLineEdit()
        self.ly.addWidget(self.label)

        self.ok_btn = QPushButton('OK')
        self.ly.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton('Cancel')
        self.ly.addWidget(self.cancel_btn)

        # Sam klass QDialog ynasledovan ot widgeta ot klassa QWidget. A znachit y nego est' method 'show'
        # No on y nas prosto otkroet okno. To est' programma prodolzit dal'she dejstvovat'  kak esli bu ja prosto otkrul
        # docechernee okno. Shto bu okno dialog zarabotalo kak dialog y nas est' fynkcija exec, no shto bu eta fynkcija shto to
        # vernyla dlja etogo est' dve specialnue fynkcii, kotorue nado  eto accept and reject

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    # Kogda y nas est' dialog i est' mnogo parametrov, nyzno sdelat' kakyjy to fynkcijy, kotoraja iz etih parametrov
    #  soberjot ydobnuj slovar'
    def getData(self):
        return dict(text=self.label.text())