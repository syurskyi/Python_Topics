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

class RemoveDocPage(QSplitter):
    def __init__(self):
        super(RemoveDocPage,self).__init__()

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
        
        input_title=QLabel(self.tr("input filter for deletes:"))
        
        self.remove_one_btn=QToolButton()
        self.remove_one_btn.setIcon(QIcon('../icon/save.svg'))
        self.remove_one_btn.setText(self.tr('delete one'))
        self.remove_one_btn.setIconSize(QSize(16,16))
        self.remove_one_btn.setToolButtonStyle(
                Qt.ToolButtonTextBesideIcon)
        self.remove_one_btn.clicked.connect(self.delete_one)

        self.remove_many_btn=QPushButton()
        self.remove_many_btn.setIcon(QIcon('../icon/save.svg'))
        self.remove_many_btn.setText(self.tr('delete many'))
        self.remove_many_btn.setIconSize(QSize(16,16))
        self.remove_many_btn.clicked.connect(self.delete_many)

        hbox=QHBoxLayout()
        hbox.addWidget(input_title,1)
        hbox.addWidget(self.remove_one_btn)
        hbox.addWidget(self.remove_many_btn)
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

    def delete_one(self):
        print('delete one')
        mongo =MongoClient()
        text=str(self.docs_edit.toPlainText().toUtf8(),
                'utf8','ignore')
        #text=self.docs_edit.toPlainText()
        print(text)
        data=json.loads(text)
        coll=mongo[self.dbname][self.collname]

        result=coll.delete_one(data)
        self.results_edit.setText(str(result.deleted_count))

    def delete_many(self):
        print('delete many')

        mongo=MongoClient()
        coll=mongo[self.dbname][self.collname]

        text=str(self.docs_edit.toPlainText())
        data=json.loads(text)
        
        result=coll.delete_many(data)
        self.results_edit.setText(str(result.deleted_count))
