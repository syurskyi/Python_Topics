'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object):
    ___ getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = l..(r..(1, n+1))
        k -= 1
        mod = 1
        ___ i __ r..(n):
            mod = mod*(i+1)
        res = ''
        ___ i __ r..(n):
            mod = mod//(n-i)
            curInd = k//mod
            k = k % mod
            res += str(nums[curInd])
            nums.pop(curInd)
        r.. res
