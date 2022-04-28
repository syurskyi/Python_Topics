'''
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
 Input: n = 4
Output: "pppz"
'''
c_ Solution:
    ___ generateTheString  n: int) -> str:
        __ n%2__0:
            r_ "a" * (n-1) + "b"
        ____
            r_ "a" * n
