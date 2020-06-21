#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
import re,json
class MongoUtils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def preview(self,col,queryjson,page,limit,sort):
        skipNum = (page - 1) * limit
        if len(queryjson.items()) > 0:
            query = json.dumps(queryjson)
        else:
            query = ""
            
        if sort == None:
            return "db."+col+".find("+query+").limit("+str(limit)+").skip("+str(skipNum)+")"
        else:
            sortStr = json.dumps(sort)
            return "db."+col+".find("+query+").sort("+sortStr+").limit("+str(limit)+").skip("+str(skipNum)+")"
       
            
            
    def parse(self,mongostmt):
        pattern = re.compile(r'db\.([\.a-zA-Z0-9]+)\.find\(({.*})\)')
        match = pattern.match(mongostmt.replace("'", "\""))
        if match:
            jsonstr = match.group(2)
            return (match.group(1),json.loads(jsonstr))
        return None

if __name__ == '__main__':
    MongoUtils()
    
    