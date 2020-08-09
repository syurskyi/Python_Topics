class Solution:
    ___ countPrimes(self, n: int) -> int:		
        
        __ n<2:
            r_ 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2,ma__.ceil(ma__.sqrt(n))):
            __ isPrime[i]:
                for multiples_of_i in range(i*i,n,i
                    isPrime[multiples_of_i] = False
        
        r_ sum(isPrime)