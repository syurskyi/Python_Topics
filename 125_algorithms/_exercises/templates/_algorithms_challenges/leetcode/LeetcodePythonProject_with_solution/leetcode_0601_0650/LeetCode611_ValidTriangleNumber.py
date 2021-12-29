'''
Created on Sep 6, 2017

@author: MT
'''
class Solution(object):
    ___ triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        ___ i __ r..(l..(nums)-1, 0, -1):
            l, r = 0, i-1
            while l < r:
                __ nums[l]+nums[r] > nums[i]:
                    count += r-l
                    r -= 1
                ____:
                    l += 1
        r.. count
    
    ___ test(self):
        testCases = [
            [2, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.triangleNumber(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
