'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    ___ toHex(self, num):
        __ num == 0: return '0'
        mp = '0123456789abcdef'
        result = ''
        for _ in range(8):
            c = mp[num&15]
            result = c + result
            num >>= 4
        return result.lstrip('0')
    
    ___ test(self):
        testCases = [
            26,
            -1,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.toHex(num)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
