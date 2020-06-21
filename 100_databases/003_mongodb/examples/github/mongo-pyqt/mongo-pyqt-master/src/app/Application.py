#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
import logging.config

from PyQt5.Qt import QApplication, QMainWindow, Qt, QAction
import sys
from model.MongoResultModel import MongoResultModel
from PyQt5 import  QtCore
from controller.AppController import AppController
from view.MainWindow import Ui_MainWindow


class Application(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
       # logging.config.fileConfig("logging.conf")
        self.log = logging.getLogger("Application")
        
        
        
    def setupModels(self):
        self.mongoResultModel = MongoResultModel()
        pass
    
    
    def setupSlot(self):
        self.ui_MainWindow.tableview.setModel(self.mongoResultModel)
        self.ui_MainWindow.connectBtn.clicked.connect(self.appctl.connectServer)
        
        self.ui_MainWindow.querybtn.clicked.connect(self.appctl.query)
        self.ui_MainWindow.query.returnPressed.connect(self.appctl.query)
        self.ui_MainWindow.query.textChanged.connect(self.appctl.queryChange)
        
        self.ui_MainWindow.tableview.clicked.connect(self.appctl.clickTable)
        self.add_query_action = QAction("add to query",self.ui_MainWindow.tableview)
        
        self.add_query_action.triggered.connect(self.appctl.addToQuery)
        self.ui_MainWindow.tableview.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui_MainWindow.tableview.addAction(self.add_query_action)
        self.tableHeader = self.ui_MainWindow.tableview.horizontalHeader()
        self.tableHeader.setSortIndicatorShown(True)
        self.tableHeader.sortIndicatorChanged.connect(self.appctl.columnSort)
        
        self.ui_MainWindow.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui_MainWindow.treeWidget.customContextMenuRequested.connect(self.appctl.showTreeMenu)
        
        self.ui_MainWindow.prevBtn.clicked.connect(self.appctl.prevPagination)
        self.ui_MainWindow.nextBtn.clicked.connect(self.appctl.nextPagination)
        
    
    
    def setupCtl(self):
        self.appctl = AppController(self)

    
    def run(self):
        self.log.info("app is start")
        
        self.qtapp = QApplication(sys.argv)
        
        self.setupUi()
        self.setupModels()
        self.setupCtl()
        self.setupSlot()
        
        
        sys.exit(self.qtapp.exec_())
        
    def setupUi(self):
        self.mainWindow = QMainWindow()
        self.ui_MainWindow = Ui_MainWindow()
        self.ui_MainWindow.setupUi(self.mainWindow)
        self.mainWindow.show()
        pass