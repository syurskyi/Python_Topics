'''
Created on Mar 18, 2019

@author: tongq
'''
class Solution(object
    ___ backspaceCompare(self, S, T
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t = S, T
        s0, t0 = '', ''
        ___ c in s:
            __ c __ '#':
                s0 = s0[:-1]
            ____
                s0 += c
        ___ c in t:
            __ c __ '#':
                t0 = t0[:-1]
            ____
                t0 += c
        r_ s0 __ t0
    
    ___ test(self
        testCases = [
            
        ]
        ___ s, t in testCases:
            result = self.backspaceCompare(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
