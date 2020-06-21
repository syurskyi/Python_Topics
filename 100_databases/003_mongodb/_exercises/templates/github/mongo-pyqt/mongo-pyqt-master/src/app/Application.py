#!/usr/bin/env python  

_______ logging.config

____ ?.Qt _______ ?A.., ?MW.., Qt, QAction
_______ ___
____ model.MongoResultModel _______ MongoResultModel
____ ? _______  ?C..
____ controller.AppController _______ AppController
____ view.MainWindow _______ Ui_MainWindow


c_ Application(object):
    '''
    classdocs
    '''


    ___  -
        '''
        Constructor
        '''
       # logging.config.fileConfig("logging.conf")
        log = logging.getLogger("Application")
        
        
        
    ___ setupModels
        mongoResultModel = MongoResultModel()
        pass
    
    
    ___ setupSlot
        ui_MainWindow.tableview.setModel(mongoResultModel)
        ui_MainWindow.connectBtn.c__.c..(appctl.connectServer)
        
        ui_MainWindow.querybtn.c__.c..(appctl.query)
        ui_MainWindow.query.returnPressed.c..(appctl.query)
        ui_MainWindow.query.textChanged.c..(appctl.queryChange)
        
        ui_MainWindow.tableview.c__.c..(appctl.clickTable)
        add_query_action = QAction("add to query",ui_MainWindow.tableview)
        
        add_query_action.triggered.c..(appctl.addToQuery)
        ui_MainWindow.tableview.setContextMenuPolicy(Qt.ActionsContextMenu)
        ui_MainWindow.tableview.addAction(add_query_action)
        tableHeader = ui_MainWindow.tableview.horizontalHeader()
        tableHeader.setSortIndicatorShown(True)
        tableHeader.sortIndicatorChanged.c..(appctl.columnSort)
        
        ui_MainWindow.treeWidget.setContextMenuPolicy(?C...Qt.CustomContextMenu)
        ui_MainWindow.treeWidget.customContextMenuRequested.c..(appctl.showTreeMenu)
        
        ui_MainWindow.prevBtn.c__.c..(appctl.prevPagination)
        ui_MainWindow.nextBtn.c__.c..(appctl.nextPagination)
        
    
    
    ___ setupCtl
        appctl = AppController(self)

    
    ___ run
        log.info("app is start")
        
        qtapp = ?A..(___.argv)
        
        setupUi()
        setupModels()
        setupCtl()
        setupSlot()
        
        
        ___.e..(qtapp.e..
        
    ___ setupUi
        mainWindow = ?MW..()
        ui_MainWindow = Ui_MainWindow()
        ui_MainWindow.setupUi(mainWindow)
        mainWindow.s..
        pass