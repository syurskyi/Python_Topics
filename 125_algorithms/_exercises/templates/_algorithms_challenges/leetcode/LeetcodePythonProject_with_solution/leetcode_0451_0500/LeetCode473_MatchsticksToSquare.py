'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object):
    ___ makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums: return False
        sumVal = sum(nums)
        __ sumVal%4 != 0: return False
        target = sumVal//4
        # Faster
        nums.sort(reverse=True)
        return self.helper(nums, [0]*4, 0, target)
    
    ___ helper(self, nums, sums, ind, target):
        __ ind == len(nums):
            __ sums[0] == target and sums[1] == target and\
                sums[2] == target and sums[3] == target:
                return True
            return False
        for i in range(4):
            __ sums[i]+nums[ind] > target:
                continue
            sums[i] += nums[ind]
            __ self.helper(nums, sums, ind+1, target):
                return True
            sums[i] -= nums[ind]
        return False
    
    ___ test(self):
        testCases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.makesquare(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
