'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    ___ dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            return -1
        first, fInd = float('-inf'), -1
        second = float('-inf')
        for i, num in enumerate(nums):
            __ num > first:
                second = first
                first = num
                fInd = i
            elif num > second:
                second = num
        return fInd __ first >= 2*second else -1
    
    ___ test(self):
        testCases = [
            [3, 6, 1, 0],
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.dominantIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
