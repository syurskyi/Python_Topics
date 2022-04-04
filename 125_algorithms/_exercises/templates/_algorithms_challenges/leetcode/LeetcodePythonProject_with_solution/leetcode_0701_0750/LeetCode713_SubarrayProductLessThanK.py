'''
Created on Oct 29, 2017

@author: MT
'''
c_ Solution(o..
    ___ numSubarrayProductLessThanK  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        __ k <_ 1: r.. 0
        prod = 1
        left = 0
        count = 0
        ___ i, num __ e..(nums
            prod *= num
            w.... left < i+1 a.. prod >_ k:
                prod //= nums[left]
                left += 1
            count += i-left+1
        r.. count
    
    ___ test
        testCases = [
            [
                [10, 5, 2, 6],
                100,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = numSubarrayProductLessThanK(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
