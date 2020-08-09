'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object
    ___ findMissingRanges(self, nums, lower, upper
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower
        for num in nums:
            __ num __ prev+1:
                res.append('%s' % prev)
            ____ num > prev+1:
                res.append('%s->%s' % (prev, min(num-1, upper)))
            prev = num+1
            __ prev > upper:
                break
        __ upper __ prev:
            res.append('%s' % prev)
        ____ upper > prev:
            res.append('%s->%s' % (prev, upper))
        r_ res
    
    ___ test(self
        testCases = [
            [
                [0,1,3,50,75],
                0, 99,
            ],
        ]
        for nums, lower, upper in testCases:
            print('nums: %s' % nums)
            print('lower: %s' % lower)
            print('upper: %s' % upper)
            result = self.findMissingRanges(nums, lower, upper)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
