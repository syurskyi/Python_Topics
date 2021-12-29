'''
Created on Mar 18, 2019

@author: tongq
'''
class Solution(object):
    ___ backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t = S, T
        s0, t0 = '', ''
        for c in s:
            __ c == '#':
                s0 = s0[:-1]
            else:
                s0 += c
        for c in t:
            __ c == '#':
                t0 = t0[:-1]
            else:
                t0 += c
        return s0 == t0
    
    ___ test(self):
        testCases = [
            
        ]
        for s, t in testCases:
            result = self.backspaceCompare(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
