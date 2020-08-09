'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object
    ___ canIWin(self, maxChoosableInteger, desiredTotal
        __ (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            r_ False
        self.memo = {}
        r_ self.helper(list(range(1, maxChoosableInteger+1)), desiredTotal)
    
    ___ helper(self, nums, desiredTotal
        hash = str(nums)
        __ hash in self.memo:
            r_ self.memo[hash]
        __ nums[-1] >= desiredTotal:
            r_ True
        length = le.(nums)
        for i in range(length
            __ not self.helper(nums[:i]+nums[i+1:], desiredTotal-nums[i]
                self.memo[hash] = True
                r_ True
        self.memo[hash] = False
        r_ False
    
    ___ test(self
        testCases = [
            [3, 11],
            [10, 11],
            [10, 40],
        ]
        for maxChoosableInteger, desiredTotal in testCases:
            print('maxChoosableInteger: %s' % maxChoosableInteger)
            print('desiredTotal: %s' % desiredTotal)
            result = self.canIWin(maxChoosableInteger, desiredTotal)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

