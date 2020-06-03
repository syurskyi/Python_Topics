#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch

'''
import sys
import logging
from PyQt5.Qt import QStandardItem,QTreeWidgetItem, QMenu, QAction, Qt,\
    QMessageBox
import pymongo
from utils.MongoUtils import MongoUtils
import json
import traceback
from PyQt5 import QtGui
import math
import time
import re
if sys.version>'3':
    import _thread as thread
else:
    import thread
'''
@property  mainWindow:QMainWindow
@property  ui:MainWindow
'''
class AppController(object):
    '''
    classdocs
    '''
    
    
    def onContextMenu(self):
        self.log.info(self.curDb+"."+self.curCol)
        self.page = 1
        self.queryjson = {}
        
        thread.start_new_thread(self.findRecord,(self.curDb,self.curCol,self.queryjson,self.page,self.limit))
#         self.findRecord(self.curDb,self.curCol,self.queryjson,self.page,self.limit)
    
    
    def __init__(self,app):
        '''
        Constructor
        '''
        self.app = app
        self.setModel(self.app.mongoResultModel)
        self.setView(self.app.ui_MainWindow)
        self.mainWindow = self.app.mainWindow
        self.mgutils = MongoUtils()
        self.sortCondition = None
        self.log = logging.getLogger("AppController")
        
        self.limit = 20
        
        self.ctxAction = QAction("Find",self.ui.treeWidget)
        self.ctxAction.triggered.connect(self.onContextMenu)
        
    def connectServer(self):
        thread.start_new_thread(self._connectServer,())
    
    def _connectServer(self):
        self.ui.connectBtn.setEnabled(False)
        host = self.ui.mongoHost.text()
        
        if host == "":
            host = "localhost"

        try:
            indexOfSep = host.index(":")
            hostName,portStr = host.split(":")
            port = int(portStr)
        except ValueError as e:
            hostName = host
            port = 27017
        
        try:
            self.conn = pymongo.Connection(hostName,port)
            self.showMsg("connect "+host+" success!")
            self.databases = self.conn.database_names()
            
                
                
            colsMap = {}
            for db in self.databases:
                colsMap[db] = self.conn[db].collection_names()
                
            self.ui.treeWidget.clear()
            treeItems = []
            for db in self.databases:
                dbItem = QTreeWidgetItem(self.ui.treeWidget,[db])
                treeItems.append(dbItem)
                cols = colsMap[db]
                for col in cols:
                    colItem = QTreeWidgetItem(dbItem,[col])
                    
                
            self.ui.treeWidget.insertTopLevelItems(0,treeItems)
            self.log.info(self.databases)
            
        except Exception as e:
            self.log.error(e)
            errorMsg = host+" connect failed:"+e.message
            self.showMsg(errorMsg)
            traceback.print_exc(file=sys.stdout)
            
        self.ui.connectBtn.setEnabled(True)
    
    
    def query(self):
        self.mongoResultModel.clear()
        query = self.ui.query.text()
        query = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", query).replace("'", "\"")
       
         
        treeItem = self.ui.treeWidget.currentItem()
        dbTreeItem = treeItem.parent()
        
        self.page = 1
        
        if dbTreeItem == None:
            self.showMsg("please select a collection")
            return
        
        collName = treeItem.text(0)
        dbName = dbTreeItem.text(0)
         
        self.curCol = collName
        self.curDb = dbName
    

        limit = self.limit
        
        
        try:
            if(query == ""):
                queryjson = {}
            else:
                queryjson = json.loads(query)
            
            
            self.queryjson = queryjson
#             self.findRecord(dbName,collName,queryjson,self.page,limit)
            thread.start_new_thread(self.findRecord,(self.curDb,self.curCol,self.queryjson,self.page,self.limit))
            
        except Exception as e:
            self.log.error(e)
            self.showMsg(e.message)
            traceback.print_exc(file=sys.stdout)
        #db = self.conn[selectDb]
    
    
    def findRecord(self, dbName, collName,queryjson,page,limit):
        self.ui.querybtn.setEnabled(False)
        preview = self.mgutils.preview(collName,queryjson,page,limit,self.sortCondition)
        self.ui.preview.setText(preview)
        
        self.ui.prevBtn.setEnabled(page > 1)
        
        
        
        db = self.conn[dbName]
        coll = db[collName]
        
       
        
        
        skipnum = (page - 1) * limit
        
        self.start = time.time()
        if self.sortCondition == None:
            cursor = coll.find(queryjson).limit(limit).skip(skipnum)
        else:
            mgSort = []
            for k,v in self.sortCondition.items():
                mgSort.append((k,v))
            
            cursor = coll.find(queryjson).sort(mgSort).limit(limit).skip(skipnum)
        
        totalCounts = cursor.count()
        pages = int(math.ceil(totalCounts/float(limit)));
        self.ui.nextBtn.setEnabled(page < pages)
        
        self.ui.paginationinfo.setText(str(self.page)+"/"+str(pages) + " total:"+str(totalCounts))
         
        self.fillTable(cursor)
        self.ui.querybtn.setEnabled(True)
    
    
    def fillTable(self,cursor):
        self.mongoResultModel.fillModelByCursor(cursor)
        self.end = time.time()
        self.ui.querytime.setText("query use:"+str('%.4f' % (self.end-self.start))+" s") 
    
    def setView(self,ui_mainWindow):
        self.ui = ui_mainWindow
        
        
    
    def setModel(self,model):
        self.mongoResultModel = model
        
    def clickTable(self):
        index = self.ui.tableview.currentIndex()
#         self.log.debug(str(index.row())+","+str(index.column())+" clicked")
        selectClickValue = self.mongoResultModel.data(index)
        
        
        
        
        self.ui.viewDetailLabel.setText(selectClickValue)
        
        
        
    def addToQuery(self):
        index = self.ui.tableview.currentIndex()
        labels = self.mongoResultModel.getLabels()
        columnName = labels[index.column()]
        
        
        self.log.debug(self.mongoResultModel.getModelData(index.row(),columnName))
        self.queryjson[columnName] = self.mongoResultModel.getModelData(index.row(),columnName)
        self.log.debug(self.queryjson)
        self.ui.query.setText(json.dumps(self.queryjson))
        
    def columnSort(self,index,order):
        labels = self.mongoResultModel.getLabels()
        columnName = labels[index]
        if order == Qt.AscendingOrder:
            mongoSort = 1
        else:
            mongoSort = -1
        
        
        self.sortCondition = {columnName:mongoSort}
        self.ui.sort.setText(json.dumps(self.sortCondition))
         
        
    def showTreeMenu(self,point):
        item = self.ui.treeWidget.itemAt(point)
        if item != None and item.parent() != None:
            self.curDb = item.parent().text(0)
            self.curCol = item.text(0)
            ctxMenu = QMenu()
            ctxMenu.addAction(self.ctxAction)
            ctxMenu.exec_(QtGui.QCursor.pos())
        
        
        
    def showMsg(self,msg):
        self.mainWindow.statusBar().showMessage(msg)
        
        
    def prevPagination(self):
        self.page -= 1
        self.pagination()
        
    def nextPagination(self): 
        self.page += 1
        self.pagination()
    
    def pagination(self):
#         self.findRecord(self.curDb, self.curCol, self.queryjson, self.page, self.limit)
        thread.start_new_thread(self.findRecord,(self.curDb,self.curCol,self.queryjson,self.page,self.limit))
        
    def queryChange(self,text):
        if text == "":
            self.queryjson={}
            
