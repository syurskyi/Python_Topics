'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..):
    ___ convertToBase7  num):
        """
        :type num: int
        :rtype: str
        """
        __ num < 0:
            num = -num
            sig = '-'
        ____:
            sig = ''
        res = ''
        w.... num > 0:
            digit = num%7
            res = s..(digit)+res
            num = i..((num-digit)/7)
        __ n.. res:
            r.. '0'
        ____:
            r.. sig+res
    
    ___ test
        testCases = [
            100,
            -7,
        ]
        ___ num __ testCases:
            result = convertToBase7(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
