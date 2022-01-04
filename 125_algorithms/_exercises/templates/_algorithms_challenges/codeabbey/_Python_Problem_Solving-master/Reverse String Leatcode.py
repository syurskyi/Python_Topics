c_ Solution:
    ___ reverse(self, x: i..) __ i..:
        __ x > 0:
            ans = i..(s..(x)[::-1])
        __ x <= 0:
            ans = -1 * i..(s..(abs(x))[::-1])
        
        mini = -2**31
        maxi = 2**31 -1
        __ ans n.. __ r..(mini,maxi):
            r.. 0
        ____:
            r.. ans
        
        