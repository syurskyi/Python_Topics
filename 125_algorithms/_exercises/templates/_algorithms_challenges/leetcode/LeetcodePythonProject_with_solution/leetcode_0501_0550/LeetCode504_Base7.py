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
        else:
            sig = ''
        res = ''
        while num > 0:
            digit = num%7
            res = str(digit)+res
            num = int((num-digit)/7)
        __ not res:
            return '0'
        else:
            return sig+res
    
    ___ test(self):
        testCases = [
            100,
            -7,
        ]
        for num in testCases:
            result = self.convertToBase7(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
