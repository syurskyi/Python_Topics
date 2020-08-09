'''
Created on Feb 23, 2017

@author: MT
'''

class Solution(object
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums: r_ []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 0
        for n in nums:
            __ n __ candidate1:
                count1 += 1
            ____ n __ candidate2:
                count2 += 1
            ____ count1 __ 0:
                candidate1, count1 = n, 1
            ____ count2 __ 0:
                candidate2, count2 = n, 1
            ____
                count1 -= 1
                count2 -= 1
        result = []
        __ nums.count(candidate1) > le.(nums)//3:
            result.append(candidate1)
        __ nums.count(candidate2) > le.(nums)//3 and candidate2 != candidate1:
            result.append(candidate2)
        r_ result
    
    ___ test(self
        testCases = [
#             [1, 2, 3],
            [2, 2, 1, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.majorityElement(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
