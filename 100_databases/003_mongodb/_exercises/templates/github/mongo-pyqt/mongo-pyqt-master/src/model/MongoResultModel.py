#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
____ ?.Qt _______ QStandardItemModel, QStandardItem
_______ ___

c_ MongoResultModel(QStandardItemModel):
    '''
    classdocs
    '''


    ___  -
        '''
        Constructor
        '''
        s__(MongoResultModel,self). - ()
    
    
    ___ fillModelByCursor(self,cursor):
        i = 0
        setheader = False
        modeldata = []
        ___ item __ cursor:
            j = 0
            items = item.items()
            
            __ setheader __ False:
                sCC..(le.(items))
                labels = item.keys()
                __ ___.version > '3':
                    labels = sorted(labels)
                ____
                    labels.sort()
                
                sHHL..(labels)
                setheader = True
                
            modeldata.append(item)
            
            ___ (field,value) __ items:
                ___
                    fieldindex = labels.index(field)
                except ValueError:
                    labels.append(field)
                    fieldindex = le.(labels) - 1
                    sHHL..(labels)
                
                valueBytes = st.(value).encode("utf_8")
                setItem(i, fieldindex, QStandardItem(valueBytes.decode(encoding='utf_8')))
                j += 1
            i += 1
        
        
    ___ getLabels
        return labels
    
    ___ getModelData(self,row,field):
        items = modeldata[row]
        __ items[field]:
            return items[field]
        ____
            print("error")
