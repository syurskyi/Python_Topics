from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient

class RenamePage(QWidget):

    def __init__(self):
        super(RenamePage,self).__init__()

        prompt=QLabel(self.tr('new name:'))
        self.name_edit=QLineEdit()

        self.ok_btn=QPushButton(self.tr('commit'))
        self.ok_btn.setIcon(QIcon('../icon/ok.svg'))
        self.ok_btn.clicked.connect(self.commit)

        self.cancel_btn=QPushButton(self.tr('cancel'))
        self.cancel_btn.setIcon(QIcon('../icon/cancel.svg'))
        self.cancel_btn.clicked.connect(self.cancel)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.ok_btn)
        hbox.addWidget(self.cancel_btn)

        vbox=QVBoxLayout()
        vbox.addWidget(prompt)
        vbox.addWidget(self.name_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def commit(self):
        print('ok')
        
        mongo=MongoClient()
        name=str(self.name_edit.text().toUtf8(),'utf-8','ignore')
        
        if self.node_type=='coll':
            dbname=str(
                    self.node.parent().parent().text(0).toUtf8(),
                    'utf-8','ignore')
            collname=str(self.node.text(0).toUtf8(),
                    'utf-8','ignore')

            coll=mongo[dbname][collname]
            coll.rename(name)
            self.node.setText(0,name)
        mongo.close()


    def cancel(self):
        print('cancel')
        self.name_edit.setText(QString())
