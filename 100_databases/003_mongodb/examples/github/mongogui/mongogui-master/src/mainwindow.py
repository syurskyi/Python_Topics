import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient
from server_info import ServerInfoPage
from finddocs import FindDocsPage
from insertdoc import InsertDocPage
from updatedoc import UpdateDocPage
from removedoc import RemoveDocPage
from createcoll import CreateCollPage
from createdb import CreateDbPage
from rename import RenamePage

class MainWindow(QMainWindow):
    c_server_node=1001
    c_db_node=1002
    c_coll_folder_node=1003
    c_func_folder_node=1004
    c_user_folder_node=1005
    c_coll_node=1101
    c_func_node=1102
    c_user_node=1103 

    def __init__(self):
        super(MainWindow,self).__init__()
        self.init_actions()
        self.init_menubar()
        self.init_toolbar()
        self.init_dbpane()

        self.tabpages=QTabWidget()
        self.tabpages.setTabsClosable(True)
        self.tabpages.tabCloseRequested.connect(self.on_page_close)

        self.splitter=QSplitter()
        self.splitter.addWidget(self.dbtree)
        self.splitter.addWidget(self.tabpages)
        self.splitter.setStretchFactor(0,0)
        self.splitter.setStretchFactor(1,1)
        
        self.setCentralWidget(self.splitter)
        self.statusBar()

        self.dbtree.setMinimumWidth(120)
        self.dbtree.setMaximumWidth(240)
        self.dbtree.resize(240,400)
        self.tabpages.resize(500,400)
        self.setGeometry(300,100,800,480)
        self.setWindowTitle(self.tr('MongoGui'))

        self.dict_page={}

    def init_actions(self):
        self.connectAction=QAction(self.tr("Connect"),self)
        self.connectAction.setIcon(QIcon('../icon/host16.svg'))
        self.connectAction.triggered.connect(self.connect)

        self.exitAction=QAction(self.tr("&Exit"),self)
        self.exitAction.setIcon(QIcon('../icon/exit16.svg'))
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setToolTip(self.tr('Exit application'))
        self.exitAction.triggered.connect(qApp.quit)

        self.aboutAction=QAction(self.tr("&About"),self)
        self.aboutAction.setToolTip(self.tr('about application'))
        self.aboutAction.triggered.connect(self.about)

        self.create_db_action = QAction(self.tr("Create db"),self)
        self.create_db_action.triggered.connect(self.create_db)

        self.remove_db_action=QAction(self.tr("remove db"),self)
        self.remove_db_action.triggered.connect(self.remove_db)

        self.console_action=QAction(self.tr("console"),self)
        self.console_action.triggered.connect(self.console)
        
        self.server_info_action=QAction(self.tr("server information"),self)
        self.server_info_action.triggered.connect(self.server_info)

        self.create_coll_action=QAction(self.tr("create collection"),self)
        self.create_coll_action.triggered.connect(self.create_coll)

        self.create_func_action=QAction(self.tr("create function"),self)
        self.create_func_action.triggered.connect(self.create_func)

        self.create_user_action=QAction(self.tr("create user"),self)
        self.create_user_action.triggered.connect(self.create_user)

        self.rename_action=QAction(self.tr("rename"),self)
        self.rename_action.triggered.connect(self.rename)

        self.clear_coll_action=QAction(self.tr("clear collections"),self)
        self.clear_coll_action.triggered.connect(self.clear_coll)

        self.list_docs_action=QAction(self.tr("show all documents"),self)
        self.list_docs_action.triggered.connect(self.list_docs)

        self.remove_coll_action=QAction(self.tr("remove collection"),self)
        self.remove_coll_action.triggered.connect(self.remove_coll)

        self.add_doc_action=QAction(self.tr("add document"),self)
        self.add_doc_action.triggered.connect(self.add_doc)

        self.remove_doc_action=QAction(self.tr("remove document"),self)
        self.remove_doc_action.triggered.connect(self.remove_doc)

        self.modify_doc_action=QAction(self.tr("modify document"),self)
        self.modify_doc_action.triggered.connect(self.modify_doc)

        self.remove_func_action=QAction(self.tr("remove function"),self)
        self.remove_func_action.triggered.connect(self.remove_func)

        self.remove_user_action=QAction(self.tr("remove user"),self)
        self.remove_user_action.triggered.connect(self.remove_user)

    def init_menubar(self):
        menubar=self.menuBar()
        self.db_menu=menubar.addMenu(self.tr('Server'))
        self.db_menu.addAction(self.connectAction)
        self.db_menu.addAction(self.exitAction)
        
        self.option_menu=menubar.addMenu(self.tr('Options'))
        self.help_menu=menubar.addMenu(self.tr('Help'))
        self.help_menu.addAction(self.aboutAction)

    def init_toolbar(self):
        self.toolbar=self.addToolBar('main')
        self.toolbar.addAction(self.connectAction)

    def init_dbpane(self):
        self.dbtree=QTreeWidget()

        self.dbtree.setHeaderLabel(self.tr('All databases'))
        
        self.dbroot_node=QTreeWidgetItem(MainWindow.c_server_node)
        self.dbroot_node.setText(0,self.tr("mongodb://localhost:27017"))
        self.dbroot_node.setIcon(0,QIcon('../icon/host16.svg'))
        
        self.dbtree.addTopLevelItem(self.dbroot_node)

        self.dbtree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dbtree.customContextMenuRequested.connect( \
                self.dbtree_contextmenu)
    
    def connect(self):
        
        self.dbroot_node.takeChildren()

        mongo=MongoClient(['localhost:27017'])
        dbnames=mongo.database_names()
        for dbname in dbnames:
            dbtree_node = QTreeWidgetItem(MainWindow.c_db_node)
            dbtree_node.setText(0,QString(dbname))
            dbtree_node.setIcon(0,QIcon('../icon/db.svg'))
            self.dbroot_node.addChild(dbtree_node)

            db = mongo.get_database(dbname)

            collections_node = \
                    QTreeWidgetItem(MainWindow.c_coll_folder_node)
            collections_node.setText(0,self.tr('collections'))
            collections_node.setIcon(0,QIcon('../icon/table.svg'))
            dbtree_node.addChild(collections_node)

            cols= db.collection_names()
            for col in cols:
                col_node = QTreeWidgetItem(MainWindow.c_coll_node)
                col_node.setText(0,QString(col))
                col_node.setIcon(0,QIcon('../icon/table.svg'))
                collections_node.addChild(col_node)

            functions_node = QTreeWidgetItem(MainWindow.c_func_folder_node)
            functions_node.setText(0,self.tr('functions'))
            functions_node.setIcon(0,QIcon('../icon/function.svg'))
            dbtree_node.addChild(functions_node)

            #funcs=db.list()
            #for func in func:
            #    func_node=QtGui.QTreeWidgetItem()
            #    func_node.setText(0,QString(func))
            #    func_node.setIcon(0,QtGui.QIcon('icon/function.svg'))
            #    functions_node.addChild(func_node)

            users_node = QTreeWidgetItem(MainWindow.c_user_folder_node)
            users_node.setText(0,self.tr('users'))
            users_node.setIcon(0,QIcon('../icon/user.svg'))
            dbtree_node.addChild(users_node)



    def about(self):
        QMessageBox.about(self,
                self.tr('about'),
                self.tr('this is a mongodb gui client')) 

    def dbtree_contextmenu(self,pos):
        item=self.dbtree.itemAt(pos)
        if item==None:
            menu=QMenu()
            menu.addAction(self.console_action)
            menu.exec_(QCursor().pos())
            return

        menu = QMenu()
        t=item.type()
        if t==MainWindow.c_server_node:
            menu.addAction(self.create_db_action)
            menu.addSeparator()
            menu.addAction(self.console_action)
            menu.addAction(self.server_info_action)
        elif t==MainWindow.c_db_node:
            menu.addAction(self.create_coll_action)
            menu.addAction(self.create_func_action)
            menu.addAction(self.create_user_action)
            menu.addSeparator()
            menu.addAction(self.remove_db_action)
            menu.addSeparator()
            menu.addAction(self.console_action)
        elif t==MainWindow.c_coll_folder_node:
            menu.addAction(self.create_coll_action)
            #menu.addAction(self.clear_coll_action)
        elif t==MainWindow.c_func_folder_node:
            menu.addAction(self.create_func_action)
        elif t==MainWindow.c_user_folder_node:
            menu.addAction(self.create_user_action)
        elif t==MainWindow.c_coll_node:
            menu.addAction(self.list_docs_action)
            menu.addAction(self.rename_action)
            menu.addAction(self.remove_coll_action)
            menu.addSeparator()
            menu.addAction(self.add_doc_action)
            menu.addAction(self.remove_doc_action)
            menu.addAction(self.modify_doc_action)
        elif t==MainWindow.c_func_node:
            menu.addAction(self.rename_action)
            menu.addAction(self.remove_func_action)
        elif t==MainWindow.c_user_node:
            menu.addAction(self.remove_user_action)

        menu.exec_(QCursor().pos())

    def on_page_close(self,index):
        print('on pag close %r' % (index))
        page=self.tabpages.widget(index)
        del self.dict_page[page.key]
        self.tabpages.removeTab(index)
        del page

    def console(self):
        print("console")

    def server_info(self):
        #client=MongoClient()
        #print client.server_info()
        current=self.dbtree.currentItem()
        if current.type()==MainWindow.c_server_node:
            server=str(current.text(0).toUtf8(),'utf-8','ignore')
            key="%s.server_info()" % (server)
            page=self.query_page(key)
            if page==None:
                page=ServerInfoPage()
                page.set_server(server)
                self.add_page(key,page)
            self.tabpages.setCurrentWidget(page)

    def create_db(self):
        print("create database")
        current=self.dbtree.currentItem()
        if current.type()==MainWindow.c_server_node:
            key="create_database()"
            page=self.query_page(key)
            if page==None:
                page=CreateDbPage()
                page.db_created.connect(self.refresh_server)
                self.add_page(key,page)

            self.tabpages.setCurrentWidget(page)

    def remove_db(self):
        print('remove db')
        current=self.dbtree.currentItem()

        client=MongoClient()
        dbname=str(current.text(0).toUtf8(),'utf-8','ignore')
        client.drop_database(dbname)
        
        parent=current.parent()
        parent.removeChild(current)

        del current

    def clear_coll(self):
        print("clear collections")

    def create_coll(self):
        print("create collection")
        
        current=self.dbtree.currentItem()
        t=current.type()
        
        dbname='test'
        dbitem=current
        if t==MainWindow.c_db_node:
            dbname=current.text(0)
            dbitem=current
        elif t==MainWindow.c_coll_folder_node:
            dbname=current.parent().text(0)
            dbitem=current.parent()
        
        key='%s.create_collection()' % dbname
        page=self.query_page(key)
        if page == None:
            page=CreateCollPage()
            page.dbitem=dbitem
            page.collection_created.connect(
                    self.refresh_collections)
            page.set_db(dbname)
            self.add_page(key,page)

        self.tabpages.setCurrentWidget(page)
    
    def create_func(self):
        print("create function")

    def create_user(self):
        print("create user")

    def rename(self):
        print("rename")
        current=self.dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.rename()" % (db,coll)
        page=self.query_page(key)

        if page==None:
            page=RenamePage()
            page.node=current
            page.node_type='coll'
            self.add_page(key,page)

        self.tabpages.setCurrentWidget(page)

    def list_docs(self):
        current=self.dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.find()" % (db,coll)
        findpage=self.query_page(key)

        if findpage==None:
            findpage=FindDocsPage()
            findpage.set_db_and_coll(db,coll)
            self.add_page(key,findpage)

        self.tabpages.setCurrentWidget(findpage)
        findpage.refresh()        

    def remove_coll(self):
        print("remove collection")
        current=self.dbtree.currentItem()
        if current.type()==MainWindow.c_coll_node:
            coll_name=str(current.text(0).toUtf8(),'utf-8','ignore')
            db_name=str(
                    current.parent().parent().text(0).toUtf8(),
                    'utf-8','ignore')
            mongo=MongoClient()
            db=mongo[db_name]
            db.drop_collection(coll_name)
            self.refresh_collections(current.parent().parent())
            mongo.close()

    def add_doc(self):
        current=self.dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.insert()" % (db,coll)
        insert_page=self.query_page(key)

        if insert_page==None:
            insert_page=InsertDocPage()
            insert_page.set_db_and_coll(db,coll)
            self.add_page(key,insert_page)

        self.tabpages.setCurrentWidget(insert_page)

    def remove_doc(self):
        current=self.dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.delete()" % (db,coll)
        del_page=self.query_page(key)

        if del_page==None:
            del_page=RemoveDocPage()
            del_page.set_db_and_coll(db,coll)
            self.add_page(key,del_page)

        self.tabpages.setCurrentWidget(del_page)

    def modify_doc(self):
        print("modify document")
        current=self.dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.update()" % (db,coll)
        update_page=self.query_page(key)

        if update_page==None:
            update_page=UpdateDocPage()
            update_page.set_db_and_coll(db,coll)
            self.add_page(key,update_page)
            
        self.tabpages.setCurrentWidget(update_page)
        

    def remove_func(self):
        print("remove function")

    def remove_user(self):
        print("remove user")

    def query_page(self,key):
        return self.dict_page.get(key)

    def add_page(self,key,page):
        self.dict_page[key]=page
        page.key=key
        self.tabpages.addTab(page,key)

    def refresh_collections(self,db_item):

        count=db_item.childCount()
        for index in range(count):
            child=db_item.child(index)
            if child.type()==MainWindow.c_coll_folder_node:
                children=child.takeChildren()
                mongo=MongoClient()
                dbname=str(db_item.text(0).toUtf8(),
                        'utf-8','ignore')
                db=mongo[dbname]
                coll_list=db.collection_names()
                for text in coll_list:
                    node=QTreeWidgetItem(MainWindow.c_coll_node)
                    node.setIcon(0,QIcon('../icon/table.svg'))
                    node.setText(0,QString(text))
                    child.addChild(node)

    def refresh_server(self,db_name):
       
        self.dbroot_node.takeChildren()
       
        mongo=MongoClient(['localhost:27017'])
        dbnames=mongo.database_names()
        for dbname in dbnames:
            dbtree_node = QTreeWidgetItem(MainWindow.c_db_node)
            dbtree_node.setText(0,QString(dbname))
            dbtree_node.setIcon(0,QIcon('../icon/db.svg'))
            self.dbroot_node.addChild(dbtree_node)

            db = mongo.get_database(dbname)

            collections_node = \
                    QTreeWidgetItem(MainWindow.c_coll_folder_node)
            collections_node.setText(0,self.tr('collections'))
            collections_node.setIcon(0,QIcon('../icon/table.svg'))
            dbtree_node.addChild(collections_node)

            cols= db.collection_names()
            for col in cols:
                col_node = QTreeWidgetItem(MainWindow.c_coll_node)
                col_node.setText(0,QString(col))
                col_node.setIcon(0,QIcon('../icon/table.svg'))
                collections_node.addChild(col_node)

            functions_node = QTreeWidgetItem(MainWindow.c_func_folder_node)
            functions_node.setText(0,self.tr('functions'))
            functions_node.setIcon(0,QIcon('../icon/function.svg'))
            dbtree_node.addChild(functions_node)

            users_node = QTreeWidgetItem(MainWindow.c_user_folder_node)
            users_node.setText(0,self.tr('users'))
            users_node.setIcon(0,QIcon('../icon/user.svg'))
            dbtree_node.addChild(users_node)

