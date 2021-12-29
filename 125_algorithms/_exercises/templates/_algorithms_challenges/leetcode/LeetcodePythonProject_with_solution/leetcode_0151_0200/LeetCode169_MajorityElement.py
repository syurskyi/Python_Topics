'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object):
    ___ majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, cand = 0, -1
        for num in nums:
            __ cand == num:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand
    
    ___ test(self):
        testCases = [
            [1, 2, 2, 3, 2],
            [5, 1, 1, 1, 3],
            [1, 1, 1, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.majorityElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ __name__ == '__main__':
    Solution().test()