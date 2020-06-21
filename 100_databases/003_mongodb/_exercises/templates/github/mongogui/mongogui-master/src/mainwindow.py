_______ ___
____ ?.?G.. _______ _
____ ?.?C.. _______ _
____ ?.?W.. _______ _

___
    ____ ?.?C.. _______ QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = st.

____ _______ _______ _______
____ server_info _______ ServerInfoPage
____ finddocs _______ FindDocsPage
____ insertdoc _______ InsertDocPage
____ updatedoc _______ UpdateDocPage
____ removedoc _______ RemoveDocPage
____ createcoll _______ CreateCollPage
____ createdb _______ CreateDbPage
____ rename _______ RenamePage

c_ MainWindow(?MW..):
    c_server_node=1001
    c_db_node=1002
    c_coll_folder_node=1003
    c_func_folder_node=1004
    c_user_folder_node=1005
    c_coll_node=1101
    c_func_node=1102
    c_user_node=1103

    ___  -
        s__(MainWindow,self). - ()
        init_actions()
        init_menubar()
        init_toolbar()
        init_dbpane()

        tabpages=QTabWidget()
        tabpages.setTabsClosable(True)
        tabpages.tabCloseRequested.c..(on_page_close)

        splitter=QSplitter()
        splitter.aW..(dbtree)
        splitter.aW..(tabpages)
        splitter.setStretchFactor(0,0)
        splitter.setStretchFactor(1,1)
        
        sCW..(splitter)
        statusBar()

        dbtree.setMinimumWidth(120)
        dbtree.setMaximumWidth(240)
        dbtree.r..(240,400)
        tabpages.r..(500,400)
        setGeometry(300,100,800,480)
        sWT..(tr('MongoGui'))

        dict_page={}

    ___ init_actions
        connectAction=QAction(tr("Connect"),self)
        connectAction.sI..(QIcon('../icon/host16.svg'))
        connectAction.triggered.c..(c..)

        exitAction=QAction(tr("&Exit"),self)
        exitAction.sI..(QIcon('../icon/exit16.svg'))
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setToolTip(tr('Exit application'))
        exitAction.triggered.c..(qApp.quit)

        aboutAction=QAction(tr("&About"),self)
        aboutAction.setToolTip(tr('about application'))
        aboutAction.triggered.c..(about)

        create_db_action = QAction(tr("Create db"),self)
        create_db_action.triggered.c..(create_db)

        remove_db_action=QAction(tr("remove db"),self)
        remove_db_action.triggered.c..(remove_db)

        console_action=QAction(tr("console"),self)
        console_action.triggered.c..(console)
        
        server_info_action=QAction(tr("server information"),self)
        server_info_action.triggered.c..(server_info)

        create_coll_action=QAction(tr("create collection"),self)
        create_coll_action.triggered.c..(create_coll)

        create_func_action=QAction(tr("create function"),self)
        create_func_action.triggered.c..(create_func)

        create_user_action=QAction(tr("create user"),self)
        create_user_action.triggered.c..(create_user)

        rename_action=QAction(tr("rename"),self)
        rename_action.triggered.c..(rename)

        clear_coll_action=QAction(tr("clear collections"),self)
        clear_coll_action.triggered.c..(clear_coll)

        list_docs_action=QAction(tr("show all documents"),self)
        list_docs_action.triggered.c..(list_docs)

        remove_coll_action=QAction(tr("remove collection"),self)
        remove_coll_action.triggered.c..(remove_coll)

        add_doc_action=QAction(tr("add document"),self)
        add_doc_action.triggered.c..(add_doc)

        remove_doc_action=QAction(tr("remove document"),self)
        remove_doc_action.triggered.c..(remove_doc)

        modify_doc_action=QAction(tr("modify document"),self)
        modify_doc_action.triggered.c..(modify_doc)

        remove_func_action=QAction(tr("remove function"),self)
        remove_func_action.triggered.c..(remove_func)

        remove_user_action=QAction(tr("remove user"),self)
        remove_user_action.triggered.c..(remove_user)

    ___ init_menubar
        menubar=menuBar()
        db_menu=menubar.addMenu(tr('Server'))
        db_menu.addAction(connectAction)
        db_menu.addAction(exitAction)
        
        option_menu=menubar.addMenu(tr('Options'))
        help_menu=menubar.addMenu(tr('Help'))
        help_menu.addAction(aboutAction)

    ___ init_toolbar
        toolbar=addToolBar('main')
        toolbar.addAction(connectAction)

    ___ init_dbpane
        dbtree=QTreeWidget()

        dbtree.setHeaderLabel(tr('All databases'))
        
        dbroot_node=QTreeWidgetItem(MainWindow.c_server_node)
        dbroot_node.sT..(0,tr("mongodb://localhost:27017"))
        dbroot_node.sI..(0,QIcon('../icon/host16.svg'))
        
        dbtree.addTopLevelItem(dbroot_node)

        dbtree.setContextMenuPolicy(Qt.CustomContextMenu)
        dbtree.customContextMenuRequested.c..( \
                dbtree_contextmenu)
    
    ___ c..
        
        dbroot_node.takeChildren()

        mongo=_______(['localhost:27017'])
        dbnames=mongo.database_names()
        ___ dbname __ dbnames:
            dbtree_node = QTreeWidgetItem(MainWindow.c_db_node)
            dbtree_node.sT..(0,QString(dbname))
            dbtree_node.sI..(0,QIcon('../icon/db.svg'))
            dbroot_node.addChild(dbtree_node)

            db = mongo.get_database(dbname)

            collections_node = \
                    QTreeWidgetItem(MainWindow.c_coll_folder_node)
            collections_node.sT..(0,tr('collections'))
            collections_node.sI..(0,QIcon('../icon/table.svg'))
            dbtree_node.addChild(collections_node)

            cols= db.collection_names()
            ___ col __ cols:
                col_node = QTreeWidgetItem(MainWindow.c_coll_node)
                col_node.sT..(0,QString(col))
                col_node.sI..(0,QIcon('../icon/table.svg'))
                collections_node.addChild(col_node)

            functions_node = QTreeWidgetItem(MainWindow.c_func_folder_node)
            functions_node.sT..(0,tr('functions'))
            functions_node.sI..(0,QIcon('../icon/function.svg'))
            dbtree_node.addChild(functions_node)

            #funcs=db.list()
            #for func in func:
            #    func_node=QtGui.QTreeWidgetItem()
            #    func_node.setText(0,QString(func))
            #    func_node.setIcon(0,QtGui.QIcon('icon/function.svg'))
            #    functions_node.addChild(func_node)

            users_node = QTreeWidgetItem(MainWindow.c_user_folder_node)
            users_node.sT..(0,tr('users'))
            users_node.sI..(0,QIcon('../icon/user.svg'))
            dbtree_node.addChild(users_node)



    ___ about
        ?MB__.about(self,
                tr('about'),
                tr('this is a mongodb gui client'))

    ___ dbtree_contextmenu(self,pos):
        item=dbtree.itemAt(pos)
        __ item__None:
            menu=QMenu()
            menu.addAction(console_action)
            menu.exec_(QCursor().pos())
            return

        menu = QMenu()
        t=item.type()
        __ t__MainWindow.c_server_node:
            menu.addAction(create_db_action)
            menu.addSeparator()
            menu.addAction(console_action)
            menu.addAction(server_info_action)
        elif t__MainWindow.c_db_node:
            menu.addAction(create_coll_action)
            menu.addAction(create_func_action)
            menu.addAction(create_user_action)
            menu.addSeparator()
            menu.addAction(remove_db_action)
            menu.addSeparator()
            menu.addAction(console_action)
        elif t__MainWindow.c_coll_folder_node:
            menu.addAction(create_coll_action)
            #menu.addAction(self.clear_coll_action)
        elif t__MainWindow.c_func_folder_node:
            menu.addAction(create_func_action)
        elif t__MainWindow.c_user_folder_node:
            menu.addAction(create_user_action)
        elif t__MainWindow.c_coll_node:
            menu.addAction(list_docs_action)
            menu.addAction(rename_action)
            menu.addAction(remove_coll_action)
            menu.addSeparator()
            menu.addAction(add_doc_action)
            menu.addAction(remove_doc_action)
            menu.addAction(modify_doc_action)
        elif t__MainWindow.c_func_node:
            menu.addAction(rename_action)
            menu.addAction(remove_func_action)
        elif t__MainWindow.c_user_node:
            menu.addAction(remove_user_action)

        menu.exec_(QCursor().pos())

    ___ on_page_close(self,index):
        print('on pag close %r' % (index))
        page=tabpages.widget(index)
        del dict_page[page.key]
        tabpages.removeTab(index)
        del page

    ___ console
        print("console")

    ___ server_info
        #client=MongoClient()
        #print client.server_info()
        current=dbtree.currentItem()
        __ current.type()__MainWindow.c_server_node:
            server=st.(current.text(0).toUtf8(),'utf-8','ignore')
            key="%s.server_info()" % (server)
            page=query_page(key)
            __ page__None:
                page=ServerInfoPage()
                page.set_server(server)
                add_page(key,page)
            tabpages.setCurrentWidget(page)

    ___ create_db
        print("create database")
        current=dbtree.currentItem()
        __ current.type()__MainWindow.c_server_node:
            key="create_database()"
            page=query_page(key)
            __ page__None:
                page=CreateDbPage()
                page.db_created.c..(refresh_server)
                add_page(key,page)

            tabpages.setCurrentWidget(page)

    ___ remove_db
        print('remove db')
        current=dbtree.currentItem()

        client=_______()
        dbname=st.(current.text(0).toUtf8(),'utf-8','ignore')
        client.drop_database(dbname)
        
        parent=current.parent()
        parent.removeChild(current)

        del current

    ___ clear_coll
        print("clear collections")

    ___ create_coll
        print("create collection")
        
        current=dbtree.currentItem()
        t=current.type()
        
        dbname='test'
        dbitem=current
        __ t__MainWindow.c_db_node:
            dbname=current.text(0)
            dbitem=current
        elif t__MainWindow.c_coll_folder_node:
            dbname=current.parent().text(0)
            dbitem=current.parent()
        
        key='%s.create_collection()' % dbname
        page=query_page(key)
        __ page __ N..:
            page=CreateCollPage()
            page.dbitem=dbitem
            page.collection_created.c..(
                    refresh_collections)
            page.set_db(dbname)
            add_page(key,page)

        tabpages.setCurrentWidget(page)
    
    ___ create_func
        print("create function")

    ___ create_user
        print("create user")

    ___ rename
        print("rename")
        current=dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.rename()" % (db,coll)
        page=query_page(key)

        __ page__None:
            page=RenamePage()
            page.node=current
            page.node_type='coll'
            add_page(key,page)

        tabpages.setCurrentWidget(page)

    ___ list_docs
        current=dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.find()" % (db,coll)
        findpage=query_page(key)

        __ findpage__None:
            findpage=FindDocsPage()
            findpage.set_db_and_coll(db,coll)
            add_page(key,findpage)

        tabpages.setCurrentWidget(findpage)
        findpage.refresh()        

    ___ remove_coll
        print("remove collection")
        current=dbtree.currentItem()
        __ current.type()__MainWindow.c_coll_node:
            coll_name=st.(current.text(0).toUtf8(),'utf-8','ignore')
            db_name=st.(
                    current.parent().parent().text(0).toUtf8(),
                    'utf-8','ignore')
            mongo=_______()
            db=mongo[db_name]
            db.drop_collection(coll_name)
            refresh_collections(current.parent().parent())
            mongo.c..

    ___ add_doc
        current=dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.insert()" % (db,coll)
        insert_page=query_page(key)

        __ insert_page__None:
            insert_page=InsertDocPage()
            insert_page.set_db_and_coll(db,coll)
            add_page(key,insert_page)

        tabpages.setCurrentWidget(insert_page)

    ___ remove_doc
        current=dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.delete()" % (db,coll)
        del_page=query_page(key)

        __ del_page__None:
            del_page=RemoveDocPage()
            del_page.set_db_and_coll(db,coll)
            add_page(key,del_page)

        tabpages.setCurrentWidget(del_page)

    ___ modify_doc
        print("modify document")
        current=dbtree.currentItem()
        db=current.parent().parent().text(0)
        coll=current.text(0)
        key="%s.%s.update()" % (db,coll)
        update_page=query_page(key)

        __ update_page__None:
            update_page=UpdateDocPage()
            update_page.set_db_and_coll(db,coll)
            add_page(key,update_page)
            
        tabpages.setCurrentWidget(update_page)
        

    ___ remove_func
        print("remove function")

    ___ remove_user
        print("remove user")

    ___ query_page(self,key):
        return dict_page.get(key)

    ___ add_page(self,key,page):
        dict_page[key]=page
        page.key=key
        tabpages.addTab(page,key)

    ___ refresh_collections(self,db_item):

        count=db_item.childCount()
        ___ index __ ra..(count):
            child=db_item.child(index)
            __ child.type()__MainWindow.c_coll_folder_node:
                children=child.takeChildren()
                mongo=_______()
                dbname=st.(db_item.text(0).toUtf8(),
                        'utf-8','ignore')
                db=mongo[dbname]
                coll_list=db.collection_names()
                ___ text __ coll_list:
                    node=QTreeWidgetItem(MainWindow.c_coll_node)
                    node.sI..(0,QIcon('../icon/table.svg'))
                    node.sT..(0,QString(text))
                    child.addChild(node)

    ___ refresh_server(self,db_name):
       
        dbroot_node.takeChildren()
       
        mongo=_______(['localhost:27017'])
        dbnames=mongo.database_names()
        ___ dbname __ dbnames:
            dbtree_node = QTreeWidgetItem(MainWindow.c_db_node)
            dbtree_node.sT..(0,QString(dbname))
            dbtree_node.sI..(0,QIcon('../icon/db.svg'))
            dbroot_node.addChild(dbtree_node)

            db = mongo.get_database(dbname)

            collections_node = \
                    QTreeWidgetItem(MainWindow.c_coll_folder_node)
            collections_node.sT..(0,tr('collections'))
            collections_node.sI..(0,QIcon('../icon/table.svg'))
            dbtree_node.addChild(collections_node)

            cols= db.collection_names()
            ___ col __ cols:
                col_node = QTreeWidgetItem(MainWindow.c_coll_node)
                col_node.sT..(0,QString(col))
                col_node.sI..(0,QIcon('../icon/table.svg'))
                collections_node.addChild(col_node)

            functions_node = QTreeWidgetItem(MainWindow.c_func_folder_node)
            functions_node.sT..(0,tr('functions'))
            functions_node.sI..(0,QIcon('../icon/function.svg'))
            dbtree_node.addChild(functions_node)

            users_node = QTreeWidgetItem(MainWindow.c_user_folder_node)
            users_node.sT..(0,tr('users'))
            users_node.sI..(0,QIcon('../icon/user.svg'))
            dbtree_node.addChild(users_node)

