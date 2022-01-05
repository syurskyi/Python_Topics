'''
Created on Apr 17, 2017

@author: MT
'''

c_ Solution(object):
    ___ arrangeCoins  n):
        start, end = 1, n
        w.... start <= end:
            mid = (start+end)/2
            __ mid*(mid+1)/2 > n:
                end = mid-1
            ____:
                start = mid+1
        r.. start-1
