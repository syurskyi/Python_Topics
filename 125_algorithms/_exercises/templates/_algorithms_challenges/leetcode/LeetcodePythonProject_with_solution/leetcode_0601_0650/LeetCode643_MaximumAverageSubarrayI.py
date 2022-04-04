'''
Created on Sep 27, 2017

@author: MT
'''
c_ Solution(o..
    ___ findMaxAverage  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        __ k <_ 0: r.. 0
        sumVal = 0
        maxVal = f__('-inf')
        ___ i, num __ e..(nums
            sumVal += num
            __ i >_ k-1:
                maxVal = m..(maxVal, sumVal)
                sumVal -= nums[i-k+1]
        r.. f__(maxVal)/k
    
    ___ test
        testCases = [
            [
                [1, 12, -5, -6, 50, 3],
                4,
            ],
            [
                [3, 3, 4, 3, 0],
                3,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = findMaxAverage(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
