#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch

'''
_______ ___
_______ logging
____ ?.Qt _______ QStandardItem,QTreeWidgetItem, QMenu, QAction, Qt,\
    ?MB__
_______ _______
____ utils.MongoUtils _______ MongoUtils
_______ json
_______ traceback
____ ? _______ ?G..
_______ math
_______ time
_______ re
__ ___.version>'3':
    _______ _thread as thread
____
    _______ thread
'''
@property  mainWindow:QMainWindow
@property  ui:MainWindow
'''
c_ AppController(object):
    '''
    classdocs
    '''
    
    
    ___ onContextMenu
        log.info(curDb+"."+curCol)
        page = 1
        queryjson = {}
        
        thread.start_new_thread(findRecord,(curDb,curCol,queryjson,page,limit))
#         self.findRecord(self.curDb,self.curCol,self.queryjson,self.page,self.limit)
    
    
    ___  - (self,app):
        '''
        Constructor
        '''
        app = app
        setModel(app.mongoResultModel)
        setView(app.ui_MainWindow)
        mainWindow = app.mainWindow
        mgutils = MongoUtils()
        sortCondition = N..
        log = logging.getLogger("AppController")
        
        limit = 20
        
        ctxAction = QAction("Find",ui.treeWidget)
        ctxAction.triggered.c..(onContextMenu)
        
    ___ connectServer
        thread.start_new_thread(_connectServer,())
    
    ___ _connectServer
        ui.connectBtn.setEnabled(False)
        host = ui.mongoHost.t..
        
        __ host __ "":
            host = "localhost"

        ___
            indexOfSep = host.index(":")
            hostName,portStr = host.split(":")
            port = int(portStr)
        except ValueError as e:
            hostName = host
            port = 27017
        
        ___
            conn = _______._______(hostName,port)
            showMsg("connect "+host+" success!")
            databases = conn.database_names()
            
                
                
            colsMap = {}
            ___ db __ databases:
                colsMap[db] = conn[db].collection_names()
                
            ui.treeWidget.c..
            treeItems = []
            ___ db __ databases:
                dbItem = QTreeWidgetItem(ui.treeWidget,[db])
                treeItems.append(dbItem)
                cols = colsMap[db]
                ___ col __ cols:
                    colItem = QTreeWidgetItem(dbItem,[col])
                    
                
            ui.treeWidget.insertTopLevelItems(0,treeItems)
            log.info(databases)
            
        except Exception as e:
            log.error(e)
            errorMsg = host+" connect failed:"
            showMsg(errorMsg)
            traceback.print_exc(file=___.stdout)
            
        ui.connectBtn.setEnabled(True)
    
    
    ___ query
        mongoResultModel.c..
        query = ui.query.t..
        query = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", query).replace("'", "\"")
       
         
        treeItem = ui.treeWidget.currentItem()
        dbTreeItem = treeItem.parent()
        
        page = 1
        
        __ dbTreeItem __ N..:
            showMsg("please select a collection")
            return
        
        collName = treeItem.text(0)
        dbName = dbTreeItem.text(0)
         
        curCol = collName
        curDb = dbName
    

        limit = limit
        
        
        ___
            __(query __ ""):
                queryjson = {}
            ____
                queryjson = json.loads(query)
            
            
            queryjson = queryjson
#             self.findRecord(dbName,collName,queryjson,self.page,limit)
            thread.start_new_thread(findRecord,(curDb,curCol,queryjson,page,limit))
            
        except Exception as e:
            log.error(e)
            showMsg(e.message)
            traceback.print_exc(file=___.stdout)
        #db = self.conn[selectDb]
    
    
    ___ findRecord(self, dbName, collName,queryjson,page,limit):
        ui.querybtn.setEnabled(False)
        preview = mgutils.preview(collName,queryjson,page,limit,sortCondition)
        ui.preview.sT..(preview)
        
        ui.prevBtn.setEnabled(page > 1)
        
        
        
        db = conn[dbName]
        coll = db[collName]
        
       
        
        
        skipnum = (page - 1) * limit
        
        start = time.time()
        __ sortCondition __ N..:
            cursor = coll.f..(queryjson).limit(limit).skip(skipnum)
        ____
            mgSort = []
            ___ k,v __ sortCondition.items():
                mgSort.append((k,v))
            
            cursor = coll.f..(queryjson).sort(mgSort).limit(limit).skip(skipnum)
        
        totalCounts = cursor.count()
        pages = int(math.ceil(totalCounts/float(limit)));
        ui.nextBtn.setEnabled(page < pages)
        
        ui.paginationinfo.sT..(st.(page)+"/"+st.(pages) + " total:"+st.(totalCounts))
         
        fillTable(cursor)
        ui.querybtn.setEnabled(True)
    
    
    ___ fillTable(self,cursor):
        mongoResultModel.fillModelByCursor(cursor)
        end = time.time()
        ui.querytime.sT..("query use:"+st.('%.4f' % (end-start))+" s")
    
    ___ setView(self,ui_mainWindow):
        ui = ui_mainWindow
        
        
    
    ___ setModel(self,model):
        mongoResultModel = model
        
    ___ clickTable
        index = ui.tableview.cI..
#         self.log.debug(str(index.row())+","+str(index.column())+" clicked")
        selectClickValue = mongoResultModel.data(index)
        
        
        
        
        ui.viewDetailLabel.sT..(selectClickValue)
        
        
        
    ___ addToQuery
        index = ui.tableview.cI..
        labels = mongoResultModel.getLabels()
        columnName = labels[index.column()]
        
        
        log.debug(mongoResultModel.getModelData(index.row(),columnName))
        queryjson[columnName] = mongoResultModel.getModelData(index.row(),columnName)
        log.debug(queryjson)
        ui.query.sT..(json.dumps(queryjson))
        
    ___ columnSort(self,index,order):
        labels = mongoResultModel.getLabels()
        columnName = labels[index]
        __ order __ Qt.AscendingOrder:
            mongoSort = 1
        ____
            mongoSort = -1
        
        
        sortCondition = {columnName:mongoSort}
        ui.sort.sT..(json.dumps(sortCondition))
         
        
    ___ showTreeMenu(self,point):
        item = ui.treeWidget.itemAt(point)
        __ item != N.. and item.parent() != N..:
            curDb = item.parent().text(0)
            curCol = item.text(0)
            ctxMenu = QMenu()
            ctxMenu.addAction(ctxAction)
            ctxMenu.exec_(?G...QCursor.pos())
        
        
        
    ___ showMsg(self,msg):
        mainWindow.statusBar().showMessage(msg)
        
        
    ___ prevPagination
        page -= 1
        pagination()
        
    ___ nextPagination
        page += 1
        pagination()
    
    ___ pagination
#         self.findRecord(self.curDb, self.curCol, self.queryjson, self.page, self.limit)
        thread.start_new_thread(findRecord,(curDb,curCol,queryjson,page,limit))
        
    ___ queryChange(self,text):
        __ text __ "":
            queryjson={}
            
