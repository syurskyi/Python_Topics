'''
Created on May 14, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isStrobogrammatic  num
        """
        :type num: str
        :rtype: bool
        """
        pairs = s..( '00', '11', '69', '96', '88' )
        singles = s..( '0', '1', '8' )
        l, r = 0, l..(num)-1
        w.... l <= r:
            __ l < r a.. num[l]+num[r] n.. __ pairs:
                r.. F..
            __ l __ r a.. num[l] n.. __ singles:
                r.. F..
            l += 1
            r -= 1
        r.. T..
