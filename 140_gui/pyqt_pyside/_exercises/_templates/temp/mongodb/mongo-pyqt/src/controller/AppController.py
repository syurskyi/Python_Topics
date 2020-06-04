______ ___
______ l__
____ ?.__ ______ QStandardItem,QTreeWidgetItem, QMenu, ?A.., __,\
    QMessageBox
______ pymongo
____ utils.MongoUtils ______ MongoUtils
______ json
______ traceback
____ ? ______ QtGui
______ math
______ time
______ re
if ___.version>'3':
    ______ _thread as thread
else:
    ______ thread
'''
@property  mainWindow:QMainWindow
@property  ui:MainWindow
'''
c_ AppController o..
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
        sM..(app.mongoResultModel)
        setView(app.ui_MainWindow)
        mainWindow = app.mainWindow
        mgutils = MongoUtils()
        sortCondition = None
        log = l__.gL..("AppController")
        
        limit = 20
        
        ctxAction = ?A..("Find",ui.tW__)
        ctxAction.t___.c__(onContextMenu)
        
    ___ connectServer
        thread.start_new_thread(_connectServer,())
    
    ___ _connectServer
        ui.cB__.setEnabled(False)
        host = ui.mongoHost.text()
        
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
            conn = pymongo.Connection(hostName,port)
            showMsg("connect "+host+" success!")
            databases = conn.database_names()
            
                
                
            colsMap = {}
            for db in databases:
                colsMap[db] = conn[db].collection_names()
                
            ui.tW__.clear()
            treeItems = []
            for db in databases:
                dbItem = QTreeWidgetItem(ui.tW__,[db])
                treeItems.append(dbItem)
                cols = colsMap[db]
                for col in cols:
                    colItem = QTreeWidgetItem(dbItem,[col])
                    
                
            ui.tW__.insertTopLevelItems(0,treeItems)
            log.info(databases)
            
        except Exception as e:
            log.error(e)
            errorMsg = host+" connect failed:"+e.message
            showMsg(errorMsg)
            traceback.print_exc(file=___.stdout)
            
        ui.cB__.setEnabled T..
    
    
    ___ query
        mongoResultModel.clear()
        query = ui.query.text()
        query = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", query).replace("'", "\"")
       
         
        treeItem = ui.tW__.currentItem()
        dbTreeItem = treeItem.parent()
        
        page = 1
        
        if dbTreeItem == None:
            showMsg("please select a collection")
            return
        
        collName = treeItem.text(0)
        dbName = dbTreeItem.text(0)
         
        curCol = collName
        curDb = dbName
    

        limit = limit
        
        
        try:
            if(query == ""):
                queryjson = {}
            else:
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
        ui.q_b_.setEnabled(False)
        preview = mgutils.preview(collName,queryjson,page,limit,sortCondition)
        ui.preview.setText(preview)
        
        ui.prevBtn.setEnabled(page > 1)
        
        
        
        db = conn[dbName]
        coll = db[collName]
        
       
        
        
        skipnum = (page - 1) * limit
        
        start = time.time()
        if sortCondition == None:
            cursor = coll.find(queryjson).limit(limit).skip(skipnum)
        else:
            mgSort = []
            for k,v in sortCondition.items():
                mgSort.append((k,v))
            
            cursor = coll.find(queryjson).sort(mgSort).limit(limit).skip(skipnum)
        
        totalCounts = cursor.count()
        pages = int(math.ceil(totalCounts/float(limit)));
        ui.nextBtn.setEnabled(page < pages)
        
        ui.paginationinfo.setText(str(page)+"/"+str(pages) + " total:"+str(totalCounts))
         
        fillTable(cursor)
        ui.q_b_.setEnabled T..
    
    
    ___ fillTable(self,cursor):
        mongoResultModel.fillModelByCursor(cursor)
        end = time.time()
        ui.querytime.setText("query use:"+str('%.4f' % (end-start))+" s")
    
    ___ setView(self,ui_mainWindow):
        ui = ui_mainWindow
        
        
    
    ___ sM..(self,model):
        mongoResultModel = model
        
    ___ clickTable
        index = ui.t_v_.currentIndex()
#         self.log.debug(str(index.row())+","+str(index.column())+" clicked")
        selectClickValue = mongoResultModel.data(index)
        
        
        
        
        ui.viewDetailLabel.setText(selectClickValue)
        
        
        
    ___ aTQ..
        index = ui.t_v_.currentIndex()
        labels = mongoResultModel.getLabels()
        columnName = labels[index.column()]
        
        
        log.debug(mongoResultModel.getModelData(index.row(),columnName))
        queryjson[columnName] = mongoResultModel.getModelData(index.row(),columnName)
        log.debug(queryjson)
        ui.query.setText(json.dumps(queryjson))
        
    ___ cS..(self,index,order):
        labels = mongoResultModel.getLabels()
        columnName = labels[index]
        if order == __.AscendingOrder:
            mongoSort = 1
        else:
            mongoSort = -1
        
        
        sortCondition = {columnName:mongoSort}
        ui.sort.setText(json.dumps(sortCondition))
         
        
    ___ showTreeMenu(self,point):
        item = ui.tW__.itemAt(point)
        if item != None and item.parent() != None:
            curDb = item.parent().text(0)
            curCol = item.text(0)
            ctxMenu = QMenu()
            ctxMenu.aA..(ctxAction)
            ctxMenu.exec_(QtGui.QCursor.pos())
        
        
        
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
        if text == "":
            queryjson={}
            
