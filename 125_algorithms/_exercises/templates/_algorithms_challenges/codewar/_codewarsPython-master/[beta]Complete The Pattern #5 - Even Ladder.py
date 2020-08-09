___ pattern(n
    __ n <= 1:
        r_ ''
    n = n-1 __ n %2 != 0 else n
    
    r_ '\n'.join([str(i) * i ___ i in range(2,n+1,2)])

___ i in range(1,10
    print(pattern(i))