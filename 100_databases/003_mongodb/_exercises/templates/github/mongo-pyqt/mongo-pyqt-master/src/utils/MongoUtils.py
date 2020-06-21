#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
_______ re,json
c_ MongoUtils(object):
    '''
    classdocs
    '''


    ___  -
        '''
        Constructor
        '''
    ___ preview(self,col,queryjson,page,limit,sort):
        skipNum = (page - 1) * limit
        __ le.(queryjson.items()) > 0:
            query = json.dumps(queryjson)
        ____
            query = ""
            
        __ sort __ N..:
            return "db."+col+".find("+query+").limit("+st.(limit)+").skip("+st.(skipNum)+")"
        ____
            sortStr = json.dumps(sort)
            return "db."+col+".find("+query+").sort("+sortStr+").limit("+st.(limit)+").skip("+st.(skipNum)+")"
       
            
            
    ___ parse(self,mongostmt):
        pattern = re.compile(r'db\.([\.a-zA-Z0-9]+)\.find\(({.*})\)')
        match = pattern.match(mongostmt.replace("'", "\""))
        __ match:
            jsonstr = match.group(2)
            return (match.group(1),json.loads(jsonstr))
        return N..

__ __name__ __ '__main__':
    MongoUtils()
    
    