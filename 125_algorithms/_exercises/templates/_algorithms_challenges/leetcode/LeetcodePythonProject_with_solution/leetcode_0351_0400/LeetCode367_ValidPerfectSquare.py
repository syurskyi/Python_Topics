'''
Created on Feb 27, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isPerfectSquare  num
        __ num <_ 0: r.. F..
        l, r 1, num//2+1
        w.... l <_ r:
            mid (l+r)//2
            __ mid*mid __ ?
                r.. T..
            ____ mid*mid > num:
                r mid-1
            ____
                l mid+1
        r.. F..
