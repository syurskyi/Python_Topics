'''
Created on Feb 7, 2017

@author: MT
'''

c_ Solution(object):
    ___ longestConsecutive(self, nums):
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
                maxLen = max(y-x, maxLen)
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

__ __name__ __ '__main__':
    Solution().test()