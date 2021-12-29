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
        __ n.. nums: r.. False
        sumVal = s..(nums)
        __ sumVal%4 != 0: r.. False
        target = sumVal//4
        # Faster
        nums.s..(r.._T..
        r.. self.helper(nums, [0]*4, 0, target)
    
    ___ helper(self, nums, sums, ind, target):
        __ ind __ l..(nums):
            __ sums[0] __ target a.. sums[1] __ target a..\
                sums[2] __ target a.. sums[3] __ target:
                r.. True
            r.. False
        ___ i __ r..(4):
            __ sums[i]+nums[ind] > target:
                continue
            sums[i] += nums[ind]
            __ self.helper(nums, sums, ind+1, target):
                r.. True
            sums[i] -= nums[ind]
        r.. False
    
    ___ test(self):
        testCases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.makesquare(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
