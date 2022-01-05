'''
Created on Feb 18, 2017

@author: MT
'''

c_ Solution(object):
    ___ isHappy  n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        hashset.add(n)
        w.... n != 1:
            num = 0
            w.... n > 0:
                num += (n % 10)**2
                n = i..(n/10)
            __ num __ hashset:
                r.. F..
            hashset.add(num)
            n = num
        r.. T..
    
    ___ test
        testCases = [
            19,
            1,
            20,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = isHappy(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
