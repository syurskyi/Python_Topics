'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ convertToBase7(self, num):
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
            num = int((num-digit)/7)
        __ n.. res:
            r.. '0'
        ____:
            r.. sig+res
    
    ___ test(self):
        testCases = [
            100,
            -7,
        ]
        ___ num __ testCases:
            result = self.convertToBase7(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
