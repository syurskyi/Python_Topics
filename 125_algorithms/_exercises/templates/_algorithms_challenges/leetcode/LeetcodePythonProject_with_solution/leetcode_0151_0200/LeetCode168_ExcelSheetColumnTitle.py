'''
Created on Feb 13, 2017

@author: MT
'''

c_ Solution(o..
    ___ convertToTitle  n
        """
        :type n: int
        :rtype: str
        """
        res ''
        w.... n > 0
            mod (n-1)%26
            res chr(mod+o..('A'+res
            n i..((n-mod)/26)
        r.. res
    
    ___ test
        ___ n __ r..(30
            print('n: %s' % (n
            result convertToTitle(n)
            print('result: %s' % (result
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()