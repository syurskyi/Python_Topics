'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object
    ___ threeSum(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = le.(nums)
        res = []
        ___ i in range(n-2
            __ i > 0 and nums[i] __ nums[i-1]:
                continue
            j, k = i+1, n-1
            w___ j < k:
                tmp = nums[i]+nums[j]+nums[k]
                __ tmp __ 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    w___ j < k and nums[j] __ nums[j-1]:
                        j += 1
                    w___ j < k and nums[k] __ nums[k+1]:
                        k -= 1
                ____ tmp > 0:
                    k -= 1
                ____
                    j += 1
        r_ res
