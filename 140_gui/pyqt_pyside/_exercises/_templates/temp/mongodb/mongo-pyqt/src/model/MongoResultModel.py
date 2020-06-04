#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
____ ?.__ ______ QStandardItemModel, QStandardItem
______ ___

c_ MongoResultModel(QStandardItemModel):
    '''
    classdocs
    '''


    ___  -
        '''
        Constructor
        '''
        super(MongoResultModel,self). - ()
    
    
    ___ fillModelByCursor(self,cursor):
        i = 0
        setheader = False
        modeldata = []
        for item in cursor:
            j = 0
            items = item.items()
            
            if setheader == False:
                setColumnCount(len(items))
                labels = item.keys()
                if ___.version > '3':
                    labels = sorted(labels)
                else:
                    labels.sort()
                
                setHorizontalHeaderLabels(labels)
                setheader = True
                
            modeldata.append(item)
            
            for (field,value) in items:
                try:
                    fieldindex = labels.index(field)
                except ValueError:
                    labels.append(field)
                    fieldindex = len(labels) - 1
                    setHorizontalHeaderLabels(labels)
                
                valueBytes = str(value).encode("utf_8")
                setItem(i, fieldindex, QStandardItem(valueBytes.decode(encoding='utf_8')))
                j += 1
            i += 1
        
        
    ___ getLabels
        return labels
    
    ___ getModelData(self,row,field):
        items = modeldata[row]
        if items[field]:
            return items[field]
        else:
            print("error")
