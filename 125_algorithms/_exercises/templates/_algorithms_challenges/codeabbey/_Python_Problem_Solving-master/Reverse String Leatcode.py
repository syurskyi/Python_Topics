class Solution:
    ___ reverse(self, x: int) -> int:
        __ x > 0:
            ans = int(str(x)[::-1])
        __ x <= 0:
            ans = -1 * int(str(abs(x))[::-1])
        
        mini = -2**31
        maxi = 2**31 -1
        __ ans n.. __ r..(mini,maxi):
            r.. 0
        ____:
            r.. ans
        
        