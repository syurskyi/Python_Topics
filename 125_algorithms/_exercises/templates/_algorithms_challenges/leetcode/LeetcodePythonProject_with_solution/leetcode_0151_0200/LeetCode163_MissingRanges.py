'''
Created on May 22, 2018

@author: tongq
'''
c_ Solution(object):
    ___ findMissingRanges  nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res    # list
        prev = lower
        ___ num __ nums:
            __ num __ prev+1:
                res.a..('%s' % prev)
            ____ num > prev+1:
                res.a..('%s->%s' % (prev, m..(num-1, upper)))
            prev = num+1
            __ prev > upper:
                break
        __ upper __ prev:
            res.a..('%s' % prev)
        ____ upper > prev:
            res.a..('%s->%s' % (prev, upper))
        r.. res
    
    ___ test
        testCases = [
            [
                [0,1,3,50,75],
                0, 99,
            ],
        ]
        ___ nums, lower, upper __ testCases:
            print('nums: %s' % nums)
            print('lower: %s' % lower)
            print('upper: %s' % upper)
            result = findMissingRanges(nums, lower, upper)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
