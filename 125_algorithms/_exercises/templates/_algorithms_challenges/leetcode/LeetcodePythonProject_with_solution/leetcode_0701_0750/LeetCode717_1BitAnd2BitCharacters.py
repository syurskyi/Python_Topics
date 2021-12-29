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
        __ not bits: return False
        n = len(bits)
        __ n == 1: return True
        dp = [1]*n
        i = 0
        while i < n:
            __ bits[i] == 1:
                i += 2
            else:
                __ i > 0:
                    dp[i] += dp[i-1]
                i += 1
        return dp[-1] > 1
    
    ___ test(self):
        testCases = [
            [1, 0, 0],
            [1, 1, 1, 0],
        ]
        for bits in testCases:
            print('bits: %s' % bits)
            result = self.isOneBitCharacter(bits)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
