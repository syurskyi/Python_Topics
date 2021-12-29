'''
Created on Oct 30, 2017

@author: MT
'''
class Solution(object):
    ___ isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        __ n.. bits: r.. False
        n = l..(bits)
        __ n __ 1: r.. True
        dp = [1]*n
        i = 0
        while i < n:
            __ bits[i] __ 1:
                i += 2
            ____:
                __ i > 0:
                    dp[i] += dp[i-1]
                i += 1
        r.. dp[-1] > 1
    
    ___ test(self):
        testCases = [
            [1, 0, 0],
            [1, 1, 1, 0],
        ]
        ___ bits __ testCases:
            print('bits: %s' % bits)
            result = self.isOneBitCharacter(bits)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
