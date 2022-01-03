___ pattern(n):
    __ n <= 0:
        r.. ''
    n = n-1 __ n %2 __ 0 ____ n
    
    r.. '\n'.j..([s..(i) * i ___ i __ r..(1,n+1,2)])

___ i __ r..(1,10):
    print(pattern(i))