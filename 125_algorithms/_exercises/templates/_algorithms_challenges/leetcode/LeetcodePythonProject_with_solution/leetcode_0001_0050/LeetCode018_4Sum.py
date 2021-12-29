'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    ___ fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = l..(nums)
        res    # list
        ___ i __ r..(n-3):
            __ i > 0 and nums[i] __ nums[i-1]:
                continue
            ___ j __ r..(i+1, n-2):
                __ j > i+1 and nums[j] __ nums[j-1]:
                    continue
                k, l = j+1, n-1
                while k < l:
                    tmp = nums[i]+nums[j]+nums[k]+nums[l]
                    __ tmp __ target:
                        res.a..([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k-1] __ nums[k]:
                            k += 1
                        while k < l and nums[l+1] __ nums[l]:
                            l -= 1
                    ____ tmp < target:
                        k += 1
                    ____:
                        l -= 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [1,0,-1,0,-2,2],
                0,
            ],
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % nums)
            result = self.fourSum(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
