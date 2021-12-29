'''
Created on Feb 21, 2018

@author: tongq
'''
class Solution(object):
    ___ pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums or len(nums) < 3: return -1
        sumVal = sum(nums)
        tmp = 0
        for i in range(len(nums)):
            __ tmp == sumVal-tmp-nums[i]:
                return i
            tmp += nums[i]
        return -1
    
    ___ test(self):
        testCases = [
            [1, 7, 3, 6, 5, 6],
            [1, 2, 3],
            [-1,-1,-1,0,1,1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.pivotIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
