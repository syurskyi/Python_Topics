'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    ___ toHex(self, num):
        __ num __ 0: r.. '0'
        mp = '0123456789abcdef'
        result = ''
        ___ _ __ r..(8):
            c = mp[num&15]
            result = c + result
            num >>= 4
        r.. result.lstrip('0')
    
    ___ test(self):
        testCases = [
            26,
            -1,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = self.toHex(num)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
