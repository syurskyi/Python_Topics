___  fact(n):
    __ n __ 0:
        r.. 1
    res = 1
    ___ i __ r..(n,0,-1):
        res = res * i
    r.. res
___ i __ r..(int(input())):
    n,k = l..(map(int,input().split()))
    result = 0
    result = fact(n) / (fact(k) * fact(n-k))
    print(int(result),end=' ')