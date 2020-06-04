#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
______ __,____
c_ MongoUtils o..
    '''
    classdocs
    '''


    ___  -
        '''
        Constructor
        '''
    ___ preview col,queryjson,page,limit,sort):
        skipNum _ (page - 1) * limit
        __ le.(queryjson.items()) > 0:
            query _ ____.dumps(queryjson)
        ____
            query _ ""
            
        __ sort __ N..
            r_ "db."+col+".find("+query+").limit("+st.(limit)+").skip("+st.(skipNum)+")"
        ____
            sortStr _ ____.dumps(sort)
            r_ "db."+col+".find("+query+").sort("+sortStr+").limit("+st.(limit)+").skip("+st.(skipNum)+")"
       
            
            
    ___ parse mongostmt):
        pattern _ __.compile(r'db\.([\.a-zA-Z0-9]+)\.find\(({.*})\)')
        match _ pattern.match(mongostmt.replace("'", "\""))
        __ match:
            jsonstr _ match.group(2)
            r_ (match.group(1),____.loads(jsonstr))
        r_ None

__ __name__ __ '__main__':
    MongoUtils()
    
    