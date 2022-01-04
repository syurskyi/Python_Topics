'''
Created on Sep 6, 2017

@author: MT
'''
c_ Solution(object):
    ___ triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.s..()
        count = 0
        ___ i __ r..(l..(nums)-1, 0, -1):
            l, r = 0, i-1
            w.... l < r:
                __ nums[l]+nums[r] > nums[i]:
                    count += r-l
                    r -= 1
                ____:
                    l += 1
        r.. count
    
    ___ test
        testCases = [
            [2, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = triangleNumber(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
