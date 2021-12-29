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
        while p % 2 == 0 and q % 2 == 0:
            p, q = p//2, q//2
        __ p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1
    
    ___ test(self):
        testCases = [
            
        ]
        for p, q in testCases:
            res = self.mirrorReflection(p, q)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
