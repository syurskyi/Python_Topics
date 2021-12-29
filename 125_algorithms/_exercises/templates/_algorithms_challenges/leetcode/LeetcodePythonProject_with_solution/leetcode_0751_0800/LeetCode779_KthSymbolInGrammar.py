'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    ___ kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        __ N __ 1:
            r.. 0
        __ K%2 __ 0:
            prev = self.kthGrammar(N-1, K/2)
            r.. 1 __ prev __ 0 ____ 0
        ____:
            prev = self.kthGrammar(N-1, (K+1)/2)
            r.. 0 __ prev __ 0 ____ 1
    
    ___ test(self):
        testCases = [
            [1, 1],
            [2, 1],
            [2, 2],
            [4, 5],
            [30, 434991989],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.kthGrammar(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
