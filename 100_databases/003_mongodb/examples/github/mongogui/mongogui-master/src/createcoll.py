from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient
# import unicode


class CreateCollPage(QWidget):
    collection_created=pyqtSignal(QTreeWidgetItem)

    def __init__(self):
        super(CreateCollPage,self).__init__()

        self.dbname='test'

        prompt=QLabel(self.tr('collection name:'))
        self.coll_name_edit=QLineEdit()

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
        vbox.addWidget(self.coll_name_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def set_db(self,dbname):
        self.dbname=str(dbname.toUtf8(),'utf-8','ignore')

    def commit(self):
        print('ok')
        
        mongo=MongoClient()
        db=mongo[self.dbname]
        collname=str(self.coll_name_edit.text().toUtf8(),
                'utf-8','ignore')
        print(collname)
        db.create_collection(collname)
        mongo.close()
        self.collection_created.emit(self.dbitem)

    def cancel(self):
        print('cancel')
        self.coll_name_edit.setText(QString())
