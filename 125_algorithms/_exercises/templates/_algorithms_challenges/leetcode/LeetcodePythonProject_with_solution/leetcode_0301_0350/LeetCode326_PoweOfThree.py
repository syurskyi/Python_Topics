'''
Created on Mar 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ isPowerOfThree  n
        __ n <_ 0: r.. F..
        r.. (3**19)%n __ 0
    
    ___ isPowerOfThreeMath  n
        __ n <_ 0: r.. F..
        w.... n > 1:
            __ n % 3 !_ 0:
                r.. F..
            n n/3
        r.. T..
