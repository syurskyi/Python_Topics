'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    ___ mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        w.... p % 2 __ 0 a.. q % 2 __ 0:
            p, q = p//2, q//2
        __ p % 2 __ 0:
            r.. 2
        ____ q % 2 __ 0:
            r.. 0
        ____:
            r.. 1
    
    ___ test(self):
        testCases = [
            
        ]
        ___ p, q __ testCases:
            res = self.mirrorReflection(p, q)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
