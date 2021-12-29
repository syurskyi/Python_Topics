'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object):
    ___ sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        c, res, MOD = 1, 0, 10**9+7
        for i in range(len(A)):
            res = (res + A[i]*c - A[len(A)-i-1]*c) % MOD
            c = (c*2)%MOD
        return (res+MOD)%MOD
    
    ___ sumSubseqWidths_own_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = []
        arr = A
        self.dfs(arr, 0, [], nums)
        res = 0
        for arr in nums:
            res = (res + max(arr) - min(arr)) % (10**9+7)
        return res
    
    ___ dfs(self, arr, idx, curr, nums):
        __ curr:
            nums.append(list(curr))
        for i in range(idx, len(arr)):
            curr.append(arr[i])
            self.dfs(arr, i+1, curr, nums)
            curr.pop()
    
    ___ test(self):
        testCases = [
            [2, 1, 3],
        ]
        for arr in testCases:
            res = self.sumSubseqWidths(arr)
            print('res: %s' % res)

__ __name__ == '__main__':
    Solution().test()
