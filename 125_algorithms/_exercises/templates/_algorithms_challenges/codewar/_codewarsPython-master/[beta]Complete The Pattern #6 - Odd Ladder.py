___ pattern(n
    __ n <= 0:
        r_ ''
    n = n-1 __ n %2 __ 0 else n
    
    r_ '\n'.join([str(i) * i ___ i __ range(1,n+1,2)])

___ i __ range(1,10
    print(pattern(i))