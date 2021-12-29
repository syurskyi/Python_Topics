'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    ___ splitArray(self, nums, m):
        left, right = 0, 0
        ___ num __ nums:
            left = max(left, num)
            right += num
        w.... left < right:
            mid = (left+right)//2
            __ self.doable(nums, m-1, mid):
                right = mid
            ____:
                left = mid+1
        r.. left
    
    ___ doable(self, nums, cuts, maxVal):
        acc = 0
        ___ num __ nums:
            __ num > maxVal:
                r.. False
            ____ acc+num <= maxVal:
                acc += num
            ____:
                cuts -= 1
                acc = num
                __ cuts < 0:
                    r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            [
                [7,2,5,10,8],
                2,
            ],
        ]
        ___ nums, m __ testCases:
            print('nums: %s' % nums)
            print('m: %s' % m)
            result = self.splitArray(nums, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
