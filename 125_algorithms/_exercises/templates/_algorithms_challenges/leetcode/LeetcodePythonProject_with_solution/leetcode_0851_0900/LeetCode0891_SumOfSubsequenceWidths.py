'''
Created on Oct 31, 2019

@author: tongq
'''
c_ Solution(object):
    ___ sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.s..()
        c, res, MOD = 1, 0, 10**9+7
        ___ i __ r..(l..(A)):
            res = (res + A[i]*c - A[l..(A)-i-1]*c) % MOD
            c = (c*2)%MOD
        r.. (res+MOD)%MOD
    
    ___ sumSubseqWidths_own_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums    # list
        arr = A
        dfs(arr, 0, [], nums)
        res = 0
        ___ arr __ nums:
            res = (res + max(arr) - m..(arr)) % (10**9+7)
        r.. res
    
    ___ dfs(self, arr, idx, curr, nums):
        __ curr:
            nums.a..(l..(curr))
        ___ i __ r..(idx, l..(arr)):
            curr.a..(arr[i])
            dfs(arr, i+1, curr, nums)
            curr.pop()
    
    ___ test
        testCases = [
            [2, 1, 3],
        ]
        ___ arr __ testCases:
            res = sumSubseqWidths(arr)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
