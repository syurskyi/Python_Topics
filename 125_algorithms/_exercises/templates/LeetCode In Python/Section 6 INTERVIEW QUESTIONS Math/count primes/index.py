c_ Solution:
    ___ countPrimes(, n: int) -> int:
        
        __ n<2:
            r_ 0
        isPrime _ [T..]*n
        isPrime[0] _ isPrime[1] _ False
        
        ___ i __ ra..(2,ma__.ceil(ma__.sqrt(n))):
            __ isPrime[i]:
                ___ multiples_of_i __ ra..(i*i,n,i
                    isPrime[multiples_of_i] _ False
        
        r_ su.(isPrime)