'''
Created on Apr 26, 2017

@author: MT
'''

c_ Solution(object):
    ___ makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums: r.. F..
        sumVal = s..(nums)
        __ sumVal%4 != 0: r.. F..
        target = sumVal//4
        # Faster
        nums.s..(r.._T..
        r.. helper(nums, [0]*4, 0, target)
    
    ___ helper(self, nums, sums, ind, target):
        __ ind __ l..(nums):
            __ sums[0] __ target a.. sums[1] __ target a..\
                sums[2] __ target a.. sums[3] __ target:
                r.. T..
            r.. F..
        ___ i __ r..(4):
            __ sums[i]+nums[ind] > target:
                continue
            sums[i] += nums[ind]
            __ helper(nums, sums, ind+1, target):
                r.. T..
            sums[i] -= nums[ind]
        r.. F..
    
    ___ test
        testCases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = makesquare(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
