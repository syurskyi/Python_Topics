'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object
    ___ primePalindrome(self, N
        """
        :type N: int
        :rtype: int
        """
        n = N
        __ 8 <= n <= 11:
            r_ 11
        for x in range(10**(le.(str(n))//2), 10**5
            y = int(str(x) + str(x)[-2::-1])
            __ y >= n and self.isPrime(y
                r_ y
    
    ___ isPrime(self, n
        __ n < 2 or n % 2 __ 0:
            r_ n __ 2
        for i in range(3, int(n**0.5)+1, 2
            __ n % i __ 0:
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            
        ]
        for n in testCases:
            res = self.primePalindrome(n)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
