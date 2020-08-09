'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object
    ___ arrangeCoins(self, n
        start, end = 1, n
        w___ start <= end:
            mid = (start+end)/2
            __ mid*(mid+1)/2 > n:
                end = mid-1
            ____
                start = mid+1
        r_ start-1
