'''
Created on Sep 30, 2019

@author: tongq
'''
c_ Solution(o..):
    ___ primePalindrome  N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        __ 8 <= n <= 11:
            r.. 11
        ___ x __ r..(10**(l..(s..(n))//2), 10**5):
            y = i..(s..(x) + s..(x)[-2::-1])
            __ y >= n a.. isPrime(y):
                r.. y
    
    ___ isPrime  n):
        __ n < 2 o. n % 2 __ 0:
            r.. n __ 2
        ___ i __ r..(3, i..(n**0.5)+1, 2):
            __ n % i __ 0:
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            
        ]
        ___ n __ testCases:
            res = primePalindrome(n)
            print('res: %s' % res)

__ _____ __ _____
    Solution().test()
