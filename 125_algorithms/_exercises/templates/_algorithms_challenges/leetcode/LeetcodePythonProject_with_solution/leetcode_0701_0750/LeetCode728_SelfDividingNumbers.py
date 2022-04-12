'''
Created on Mar 4, 2018

@author: tongq
'''
c_ Solution(o..
    ___ selfDividingNumbers  left, right
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res    # list
        ___ num __ r..(left, right+1
            __ isSelfDividing(num
                res.a..(num)
        r.. res
        
    ___ isSelfDividing  num
        ___ digit __ s..(num
            d i..(digit)
            __ d __ 0 o. num_d !_ 0:
                r.. F..
        r.. T..
    
    ___ test
        testCases [
            [1, 22],
        ]
        ___ left, right __ testCases:
            print('left: %s' % left)
            print('right: %s' % right)
            result selfDividingNumbers(left, right)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
