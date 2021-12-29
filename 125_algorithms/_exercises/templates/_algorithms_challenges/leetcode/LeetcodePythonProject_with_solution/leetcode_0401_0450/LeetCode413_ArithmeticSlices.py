'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    ___ numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = A
        __ n.. nums o. l..(nums) < 3: r.. 0
        res = 0
        curr = 0
        ___ i __ r..(2, l..(nums)):
            __ nums[i]-nums[i-1] __ nums[i-1]-nums[i-2]:
                curr += 1
            ____:
                curr = 0
            res += curr
        r.. res
    
    ___ test(self):
        testCases = [
            [1, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
