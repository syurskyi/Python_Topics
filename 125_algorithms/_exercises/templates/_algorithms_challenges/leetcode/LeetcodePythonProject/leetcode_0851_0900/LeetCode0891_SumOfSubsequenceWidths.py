'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object
    ___ sumSubseqWidths(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        c, res, MOD = 1, 0, 10**9+7
        ___ i in range(le.(A)):
            res = (res + A[i]*c - A[le.(A)-i-1]*c) % MOD
            c = (c*2)%MOD
        r_ (res+MOD)%MOD
    
    ___ sumSubseqWidths_own_TLE(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        nums = []
        arr = A
        self.dfs(arr, 0, [], nums)
        res = 0
        ___ arr in nums:
            res = (res + max(arr) - min(arr)) % (10**9+7)
        r_ res
    
    ___ dfs(self, arr, idx, curr, nums
        __ curr:
            nums.append(list(curr))
        ___ i in range(idx, le.(arr)):
            curr.append(arr[i])
            self.dfs(arr, i+1, curr, nums)
            curr.pop()
    
    ___ test(self
        testCases = [
            [2, 1, 3],
        ]
        ___ arr in testCases:
            res = self.sumSubseqWidths(arr)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
