'''
Created on Apr 2, 2017

@author: MT
'''

c_ Solution(o..
    ___ lastRemaining  n
        left = T..
        remaining = n
        head = 1
        step = 1
        w.... remaining > 1:
            __ left o. remaining%2__1:
                head += step
            remaining //= 2
            step *= 2
            left = n.. left
        r.. head
    
    ___ test
        testCases = [
            9
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = lastRemaining(num)
            print('result1: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
