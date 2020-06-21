from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient
import json

class InsertDocPage(QSplitter):
    def __init__(self):
        super(InsertDocPage,self).__init__()

        self.dbname='test'
        self.collname=''

        #self.toolbar=QToolBar()
        #self.toolbar.setIconSize(QSize(16,16))
        #self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        #self.commit_act=self.toolbar.addAction(
        #        QIcon('../icon/save.svg'),
        #        self.tr('commit'))
        #self.commit_act.triggered.connect(self.commit)
        
        #self.splitter=QSplitter()
        self.input_view=QWidget()
        input_header=QWidget()
        
        input_title=QLabel(self.tr("input inserted documents:"))
        self.commit_btn=QToolButton()
        self.commit_btn.setIcon(QIcon('../icon/save.svg'))
        self.commit_btn.setText(self.tr('commit'))
        self.commit_btn.setIconSize(QSize(16,16))
        self.commit_btn.setToolButtonStyle(
                Qt.ToolButtonTextBesideIcon)
        self.commit_btn.clicked.connect(self.commit)
        hbox=QHBoxLayout()
        hbox.addWidget(input_title,1)
        hbox.addWidget(self.commit_btn)
        hbox.setMargin(0)
        hbox.setSpacing(0)
        input_header.setLayout(hbox)

        self.docs_edit=QTextEdit()

        vbox=QVBoxLayout()
        vbox.addWidget(input_header)
        vbox.addWidget(self.docs_edit,1)
        vbox.setMargin(0)
        vbox.setSpacing(0)
        self.input_view.setLayout(vbox)

        self.results_view=QWidget()
        results_header=QLabel(self.tr("results:"))
        self.results_edit=QTextEdit()
        results_vbox=QVBoxLayout()
        results_vbox.addWidget(results_header)
        results_vbox.addWidget(self.results_edit,1)
        results_vbox.setMargin(0)
        results_vbox.setSpacing(0)
        self.results_view.setLayout(results_vbox)

        self.addWidget(self.input_view)
        self.addWidget(self.results_view)

        self.setOrientation(Qt.Vertical)

        #vbox=QVBoxLayout()
        #vbox.addWidget(self.toolbar)
        #vbox.addWidget(self.splitter,1)
        #vbox.setMargin(0)
        #vbox.setSpacing(0)
        #self.setLayout(vbox)

    def set_db_and_coll(self,dbname,collname):
        self.dbname=str(dbname)
        self.collname=str(collname)

    def commit(self):
        print('commit')
        mongo =MongoClient()
        text=str(self.docs_edit.toPlainText().toUtf8(),
                'utf8','ignore')
        #text=self.docs_edit.toPlainText()
        print(text)
        data=json.loads(text)
        coll=mongo[self.dbname][self.collname]
        if isinstance(data,dict):
            result=coll.insert_one(data)
            self.results_edit.setText(str(result.inserted_id))
        else:
            result=coll.insert_many(data)
            self.results_edit.setText(str(result.inserted_ids))

