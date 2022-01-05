'''
Created on Apr 23, 2017

@author: MT
'''

c_ Solution(o..):
    ___ hammingDistance  x, y):
        count = 0
        ___ i __ r..(32):
            count += (x>>i&1)^(y>>i&1)
        r.. count
    
    ___ test
        testCases = [
            [1, 4],
        ]
        ___ x, y __ testCases:
            print('x: %s' % x)
            print('y: %s' % y)
            result = hammingDistance(x, y)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
