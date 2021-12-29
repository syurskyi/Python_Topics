'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object):
    ___ primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        __ 8 <= n <= 11:
            r.. 11
        ___ x __ r..(10**(l..(s..(n))//2), 10**5):
            y = int(s..(x) + s..(x)[-2::-1])
            __ y >= n a.. self.isPrime(y):
                r.. y
    
    ___ isPrime(self, n):
        __ n < 2 o. n % 2 __ 0:
            r.. n __ 2
        ___ i __ r..(3, int(n**0.5)+1, 2):
            __ n % i __ 0:
                r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            
        ]
        ___ n __ testCases:
            res = self.primePalindrome(n)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
