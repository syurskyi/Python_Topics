'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    ___ splitArray(self, nums, m):
        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num
        while left < right:
            mid = (left+right)//2
            __ self.doable(nums, m-1, mid):
                right = mid
            else:
                left = mid+1
        return left
    
    ___ doable(self, nums, cuts, maxVal):
        acc = 0
        for num in nums:
            __ num > maxVal:
                return False
            elif acc+num <= maxVal:
                acc += num
            else:
                cuts -= 1
                acc = num
                __ cuts < 0:
                    return False
        return True
    
    ___ test(self):
        testCases = [
            [
                [7,2,5,10,8],
                2,
            ],
        ]
        for nums, m in testCases:
            print('nums: %s' % nums)
            print('m: %s' % m)
            result = self.splitArray(nums, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
