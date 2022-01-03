'''
Created on Mar 2, 2017

@author: MT
'''

c_ Solution(object):
    ___ threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.s..()
        res = 0
        ___ i __ r..(l..(nums)-2):
            j, k = i+1, l..(nums)-1
            w.... j < k:
                __ nums[i]+nums[j]+nums[k] >= target:
                    k -= 1
                ____:
                    res += k-j
                    j += 1
        r.. res
    
    ___ test
        testCases = [
            ([-2, 0, 1, 3], 2),
            ([3, 1, 0, -2], 4),
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % (nums))
            print('target: %s' % (target))
            result = threeSumSmaller(nums, target)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
