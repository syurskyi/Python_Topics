'''
Created on Oct 1, 2017

@author: MT
'''
c_ Solution(o..
    ___ findErrorNums  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset = s..()
        n = l..(nums)
        sumVal = n*(n+1)//2
        res    # list
        ___ num __ nums:
            __ num n.. __ hashset:
                hashset.add(num)
                sumVal -= num
            ____
                res.a..(num)
        res.a..(sumVal)
        r.. res
    
    ___ test
        testCases = [
            [1, 2, 2, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findErrorNums(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
