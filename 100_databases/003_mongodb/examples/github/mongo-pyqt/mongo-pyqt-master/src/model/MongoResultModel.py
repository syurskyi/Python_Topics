#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
from PyQt5.Qt import QStandardItemModel, QStandardItem
import sys

class MongoResultModel(QStandardItemModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MongoResultModel,self).__init__()
    
    
    def fillModelByCursor(self,cursor):
        i = 0
        setheader = False
        self.modeldata = []
        for item in cursor:
            j = 0
            items = item.items()
            
            if setheader == False:
                self.setColumnCount(len(items))
                self.labels = item.keys()
                if sys.version > '3':
                    self.labels = sorted(self.labels)
                else:
                    self.labels.sort()
                
                self.setHorizontalHeaderLabels(self.labels)
                setheader = True
                
            self.modeldata.append(item)
            
            for (field,value) in items:
                try:
                    fieldindex = self.labels.index(field)
                except ValueError:
                    self.labels.append(field)
                    fieldindex = len(self.labels) - 1
                    self.setHorizontalHeaderLabels(self.labels)
                
                valueBytes = str(value).encode("utf_8")
                self.setItem(i, fieldindex, QStandardItem(valueBytes.decode(encoding='utf_8')))
                j += 1
            i += 1
        
        
    def getLabels(self):
        return self.labels
    
    def getModelData(self,row,field):
        items = self.modeldata[row]
        if items[field]:
            return items[field]
        else:
            print("error")
