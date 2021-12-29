'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    ___ threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        n = l..(nums)
        ___ i __ r..(n-2):
            j, k = i+1, n-1
            while j < k:
                tmp = nums[i]+nums[j]+nums[k]
                diff = abs(tmp-target)
                __ diff < abs(res-target):
                    res = tmp
                __ tmp __ target:
                    r.. target
                ____ tmp > target:
                    k -= 1
                ____:
                    j += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [-1, 2, 1, -4],
                1,
            ],
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % nums)
            print('target: %s' % target)
            result = self.threeSumClosest(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
