'''
Created on Feb 7, 2017

@author: MT
'''

c_ Solution(o..):
    ___ longestConsecutive  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxLen = 0
        ___ x __ nums:
            __ x-1 n.. __ nums:
                y = x+1
                w.... y __ nums:
                    y+=1
                maxLen = m..(y-x, maxLen)
        r.. maxLen
    
    ___ test
        testCases = [
            [100, 4, 200, 1, 3, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = longestConsecutive(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()