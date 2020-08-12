# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:43:24 2017
beispiel https://youtu.be/F1ODsSWi9nk?list=PLNmsVeXQZj7q0ao69AIogD94oBgp3E9Zs
@author: mom
"""
import logging

logging.basicConfig(level=logging.DEBUG)
form = logging.Formatter('%(name)s # %(levelname)s : %(asctime)s\n\t %(message)s')
fileH = logging.FileHandler('log.me', mode = 'w')
fileH.setFormatter(form)
logger = logging.getLogger()
                        
logger.addHandler(fileH) 
                       

logger.debug('test Debug')  
#logging.debug('debug')
#logging.warning('warning')
#logging.info('info')
#logging.error('error')
#logging.critical('critical')







def testFunktion():
    logger = logging.getLogger("testFunktion")
    logger.setLevel(logging.DEBUG)
    logger.debug('run testFunktion')



testFunktion()