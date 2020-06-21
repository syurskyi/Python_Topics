from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient

class CreateDbPage(QWidget):
    db_created=pyqtSignal(str)

    def __init__(self):
        super(CreateDbPage,self).__init__()

        prompt=QLabel(self.tr('database name:'))
        self.dbname_edit=QLineEdit()

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
        vbox.addWidget(self.dbname_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def commit(self):
        print('ok')
        
        mongo=MongoClient()
        dbname=str(self.dbname_edit.text().toUtf8(),'utf-8','ignore')
        print(dbname)
        db=mongo.get_database(dbname)
        db.create_collection('temp')
        mongo.close()

        client=MongoClient()
        db=client[dbname]
        db.drop_collection('temp')
        client.close()

        self.db_created.emit(dbname)

    def cancel(self):
        print('cancel')
        self.coll_name_edit.setText(QString())
