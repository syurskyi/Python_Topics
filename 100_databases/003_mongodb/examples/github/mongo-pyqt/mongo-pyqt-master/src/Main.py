#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''
Created on 2014年9月20日

@author: wanghch
'''
import sys
import importlib
from app.Application import Application
if sys.version<'3':
    importlib.reload(sys)
    sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
    app = Application()
    app.run()
    
    pass