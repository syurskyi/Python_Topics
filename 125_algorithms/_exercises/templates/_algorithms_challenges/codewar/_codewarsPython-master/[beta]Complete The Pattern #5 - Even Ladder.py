___ pattern(n):
    __ n <= 1:
        r.. ''
    n = n-1 __ n %2 != 0 ____ n
    
    r.. '\n'.join([s..(i) * i ___ i __ r..(2,n+1,2)])

___ i __ r..(1,10):
    print(pattern(i))