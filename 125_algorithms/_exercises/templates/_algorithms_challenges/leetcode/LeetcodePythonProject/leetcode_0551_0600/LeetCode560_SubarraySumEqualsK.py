'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object
    ___ subarraySum(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0:1}
        sumVal = 0
        res = 0
        for num in nums:
            sumVal += num
            __ sumVal-k in hashmap:
                res += hashmap[sumVal-k]
            hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        r_ res
    
    ___ test(self
        testCases = [
            [
                [1, 1, 1],
                2,
            ],
            [
                [1, 1, 1],
                3,
            ],
            [
                [1, 1, 1],
                1,
            ],
            [
                [1, 1, 1],
                0,
            ],
            [
                [1, -1, 1, -1, 2,-2],
                0,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            res = self.subarraySum(nums, k)
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
