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

class UpdateDocPage(QWidget):
    def __init__(self):
        super(UpdateDocPage,self).__init__()

        self.dbname='test'
        self.collname=''

        self.toolbar=QToolBar()
        self.toolbar.setIconSize(QSize(16,16))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.update_one_act=self.toolbar.addAction(
                QIcon('../icon/save.svg'),
                self.tr('update one'))
        self.update_one_act.triggered.connect(self.update_one)
        
        self.update_many_act=self.toolbar.addAction(
                QIcon('../icon/save.svg'),
                self.tr('update many'))
        self.update_many_act.triggered.connect(self.update_many)

        self.replace_act=self.toolbar.addAction(
                QIcon('../icon/replace.svg'),
                self.tr('replace one'))
        self.replace_act.triggered.connect(self.replace)
        
        self.hsplitter=QSplitter()
        
        self.filter_view=QWidget()
        filter_header=QLabel(self.tr("filter:"))
        self.filter_edit=QTextEdit()
        filter_vbox=QVBoxLayout()
        filter_vbox.addWidget(filter_header)
        filter_vbox.addWidget(self.filter_edit,1)
        filter_vbox.setMargin(0)
        filter_vbox.setSpacing(0)
        self.filter_view.setLayout(filter_vbox)

        self.update_view=QWidget()
        update_header=QLabel(self.tr("update:"))
        self.update_edit=QTextEdit()
        header_vbox=QVBoxLayout()
        header_vbox.addWidget(update_header)
        header_vbox.addWidget(self.update_edit,1)
        header_vbox.setMargin(0)
        header_vbox.setSpacing(0)
        self.update_view.setLayout(header_vbox)

        self.hsplitter.addWidget(self.filter_view)
        self.hsplitter.addWidget(self.update_view)

        self.splitter=QSplitter()
        self.results_view=QWidget()
        results_header=QLabel(self.tr("results:"))
        self.results_edit=QTextEdit()
        results_vbox=QVBoxLayout()
        results_vbox.addWidget(results_header)
        results_vbox.addWidget(self.results_edit,1)
        results_vbox.setMargin(0)
        results_vbox.setSpacing(0)
        self.results_view.setLayout(results_vbox)

        self.splitter.addWidget(self.hsplitter)
        self.splitter.addWidget(self.results_view)

        self.splitter.setOrientation(Qt.Vertical)

        vbox=QVBoxLayout()
        vbox.addWidget(self.toolbar)
        vbox.addWidget(self.splitter,1)
        vbox.setMargin(0)
        vbox.setSpacing(0)
        self.setLayout(vbox)

    def set_db_and_coll(self,dbname,collname):
        self.dbname=str(dbname)
        self.collname=str(collname)

    def update_one(self):
        print('update one')
        
        mongo =MongoClient()
        coll=mongo[self.dbname][self.collname]

        filter_text=str(self.filter_edit.toPlainText().toUtf8(),
                'utf8','ignore')
        update_text=str(self.update_edit.toPlainText().toUtf8(),
                'utf8','ignore')

        print(filter_text)
        print(update_text)

        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)
        
        result=coll.update_one(filter_data,update_data)
        
        self.results_edit.setText(
                'matched count:%r \nmodified count:%r' % (
                    result.matched_count,
                    result.modified_count))
        mongo.close()

    def update_many(self):
        print('update many')
        
        mongo=MongoClient()
        coll = mongo[self.dbname][self.collname]

        filter_text=str(self.filter_edit.toPlainText())
        update_text=str(self.update_edit.toPlainText())
        
        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)
        
        result=coll.update_many(filter_data,update_data)
        self.results_edit.setText(
                'matched count:%r \nmodified count:%r' % (
                    result.matched_count,
                    result.modified_count))

        mongo.close()

    def replace(self):
        print('replace one')
        mongo=MongoClient()
        coll=mongo[self.dbname][self.collname]

        filter_text=str(self.filter_edit.toPlainText())
        update_text=str(self.update_edit.toPlainText())

        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)

        result=coll.replace_one(filter_data,update_data)
        self.results_edit.setText(
                    'matched count:%r \nmodified count:%r' %(
                        result.matched_count,
                        result.modified_count))
        
        mongo.close()
