'''
Created on Oct 5, 2017

@author: MT
'''
class Solution(object):
    ___ cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        nums = A
        __ not nums or nums[-1] == -1: return []
        res = []
        n = len(nums)
        dp = [float('inf')]*n
        dp[-1] = nums[-1]
        pos = [-1]*n
        for i in range(n-2, -1, -1):
            __ nums[i] == -1:
                continue
            for j in range(i+1, min(i+B, n-1)+1):
                __ dp[j] == float('inf'):
                    continue
                __ nums[i]+dp[j] < dp[i]:
                    dp[i] = nums[i]+dp[j]
                    pos[i] = j
        __ dp[0] == float('inf'):
            return res
        ind = 0
        while ind != -1:
            res.append(ind+1)
            ind = pos[ind]
        return res
    
    ___ test(self):
        testCases = [
            [
                [1, 2, 4, -1, 2],
                2,
            ],
            [
                [1, 2, 4, -1, 2],
                1
            ],
            [
                [0, 0, 0, 0, 0, 0],
                3,
            ],
        ]
        for a, b in testCases:
            print('a: %s' % a)
            print('b: %s' % b)
            result = self.cheapestJump(a, b)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
