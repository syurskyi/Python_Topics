'''
Created on Feb 13, 2017

@author: MT
'''

c_ Solution(object):
    ___ titleToNumber  s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        ___ c __ s:
            result = result*26
            num = o..(c)-o..('A')+1
            result += num
        r.. result
    
    ___ test
        testCases = [
            'A',
            'B',
            'Z',
            'AA',
            'AAA',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = titleToNumber(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()