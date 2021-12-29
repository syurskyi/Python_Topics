'''
Created on Feb 7, 2017

@author: MT
'''

class Solution(object):
    ___ longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxLen = 0
        for x in nums:
            __ x-1 not in nums:
                y = x+1
                while y in nums:
                    y+=1
                maxLen = max(y-x, maxLen)
        return maxLen
    
    ___ test(self):
        testCases = [
            [100, 4, 200, 1, 3, 2],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.longestConsecutive(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()