'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ canIWin(self, maxChoosableInteger, desiredTotal):
        __ (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            r.. False
        self.memo = {}
        r.. self.helper(l..(r..(1, maxChoosableInteger+1)), desiredTotal)
    
    ___ helper(self, nums, desiredTotal):
        hash = str(nums)
        __ hash __ self.memo:
            r.. self.memo[hash]
        __ nums[-1] >= desiredTotal:
            r.. True
        length = l..(nums)
        ___ i __ r..(length):
            __ n.. self.helper(nums[:i]+nums[i+1:], desiredTotal-nums[i]):
                self.memo[hash] = True
                r.. True
        self.memo[hash] = False
        r.. False
    
    ___ test(self):
        testCases = [
            [3, 11],
            [10, 11],
            [10, 40],
        ]
        ___ maxChoosableInteger, desiredTotal __ testCases:
            print('maxChoosableInteger: %s' % maxChoosableInteger)
            print('desiredTotal: %s' % desiredTotal)
            result = self.canIWin(maxChoosableInteger, desiredTotal)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

