'''
Created on Feb 11, 2017

@author: MT
'''
c_ Solution(o..
    ___ maxProduct  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n l..(nums)
        maxArr, minArr [0]*n, [0]*n
        maxArr[0], minArr[0] nums[0], nums[0]
        result nums[0]
        ___ i __ r..(1, n
            num nums[i]
            __ num > 0
                maxArr[i] m..(maxArr[i-1]*num, num)
                minArr[i] m..(minArr[i-1]*num, num)
            ____
                maxArr[i] m..(minArr[i-1]*num, num)
                minArr[i] m..(maxArr[i-1]*num, num)
            result m..(result, maxArr[i])
        r.. ?
    
    ___ test
        testCases [
            [2, 3, -2, 4],
            [1, 0, 9, 10, -19, 2000],
            [100, 2, -1, 9, 89, -1, -1, 9],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result maxProduct(nums)
            print('result: %s' % (result
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()
