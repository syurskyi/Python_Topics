'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object
    ___ makesquare(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums: r_ False
        sumVal = sum(nums)
        __ sumVal%4 != 0: r_ False
        target = sumVal//4
        # Faster
        nums.sort(reverse=True)
        r_ self.helper(nums, [0]*4, 0, target)
    
    ___ helper(self, nums, sums, ind, target
        __ ind __ le.(nums
            __ sums[0] __ target and sums[1] __ target and\
                sums[2] __ target and sums[3] __ target:
                r_ True
            r_ False
        for i in range(4
            __ sums[i]+nums[ind] > target:
                continue
            sums[i] += nums[ind]
            __ self.helper(nums, sums, ind+1, target
                r_ True
            sums[i] -= nums[ind]
        r_ False
    
    ___ test(self
        testCases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.makesquare(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
