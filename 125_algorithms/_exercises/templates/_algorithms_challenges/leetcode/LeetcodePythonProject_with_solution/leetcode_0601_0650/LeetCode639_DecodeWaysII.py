'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object):
    ___ numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        e0, e1, e2 = 1, 0, 0
        ___ c __ s:
            __ c __ '*':
                f0 = e0*9 + e1*9 + e2*6
                f1 = e0
                f2 = e0
            ____:
                f0 = e0*(c>'0') + e1 + e2*(c<='6')
                f1 = e0*(c__'1')
                f2 = e0*(c__'2')
            e0, e1, e2 = f0%MOD, f1, f2
        r.. e0
    
    ___ test(self):
        testCases = [
            '*',
            '1*',
            '*1*1*0',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.numDecodings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
