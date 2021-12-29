'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object):
    ___ findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        n = l..(nums)
        i = 0
        res = 1
        w.... i < n:
            j = i
            w.... i+1 < n a.. nums[i] < nums[i+1]:
                i += 1
                res = max(res, i-j+1)
            i += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findLengthOfLCIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
