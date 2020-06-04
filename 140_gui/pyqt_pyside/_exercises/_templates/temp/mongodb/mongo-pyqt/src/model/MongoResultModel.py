#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
____ ?.__ ______ QStandardItemModel, ?SI..
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
    
    
    ___ fillModelByCursor cursor):
        i _ 0
        setheader _ False
        modeldata _   # list
        ___ item in cursor:
            j _ 0
            items _ item.items()
            
            __ setheader __ False:
                setColumnCount(len(items))
                labels _ item.keys()
                __ ___.version > '3':
                    labels _ sorted(labels)
                ____
                    labels.sort()
                
                setHorizontalHeaderLabels(labels)
                setheader _ True
                
            modeldata.ap..(item)
            
            ___ (field,value) in items:
                ___
                    fieldindex _ labels.index(field)
                ______ V..:
                    labels.ap..(field)
                    fieldindex _ len(labels) - 1
                    setHorizontalHeaderLabels(labels)
                
                valueBytes _ st.(value).encode("utf_8")
                setItem(i, fieldindex, ?SI..(valueBytes.decode(encoding_'utf_8')))
                j +_ 1
            i +_ 1
        
        
    ___ getLabels
        r_ labels
    
    ___ getModelData row,field):
        items _ modeldata[row]
        __ items[field]:
            r_ items[field]
        ____
            print("error")
