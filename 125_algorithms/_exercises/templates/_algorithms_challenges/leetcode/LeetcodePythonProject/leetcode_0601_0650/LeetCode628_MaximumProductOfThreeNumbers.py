'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object
    ___ maximumProduct(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums or le.(nums) < 3:
            r_ 0
        s1, s2 = float('inf'), float('inf')
        l1, l2, l3 = float('-inf'), float('-inf'), float('-inf')
        ___ num in nums:
            __ num < s1:
                s2 = s1
                s1 = num
            ____ num < s2:
                s2 = num
            __ num > l1:
                l3 = l2
                l2 = l1
                l1 = num
            ____ num > l2:
                l3 = l2
                l2 = num
            ____ num > l3:
                l3 = num
        res = float('-inf')
        ___ a1, a2, a3 in (l1, l2, l3), (s1, s2, l1
            res = max(res, a1*a2*a3)
        r_ res
    
    ___ test(self
        testCases = [
            [1,2,3],
            [1,2,3,4],
            [-1, -2, 0, 3],
            [-1, -2, -3, 1],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.maximumProduct(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
