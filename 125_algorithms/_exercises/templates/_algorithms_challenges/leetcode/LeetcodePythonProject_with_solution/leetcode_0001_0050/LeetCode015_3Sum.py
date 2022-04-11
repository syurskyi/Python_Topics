'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ threeSum  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.s..()
        n = l..(nums)
        res    # list
        ___ i __ r..(n-2
            __ i > 0 a.. nums[i] __ nums[i-1]:
                _____
            j, k = i+1, n-1
            w.... j < k:
                tmp  nums[i]+nums[j]+nums[k]
                __ tmp __ 0:
                    res.a..([nums[i], nums[j], nums[k]])
                    j += 1
                    k -_ 1
                    w.... j < k a.. nums[j] __ nums[j-1]:
                        j += 1
                    w.... j < k a.. nums[k] __ nums[k+1]:
                        k -_ 1
                ____ tmp > 0:
                    k -_ 1
                ____
                    j += 1
        r.. res
