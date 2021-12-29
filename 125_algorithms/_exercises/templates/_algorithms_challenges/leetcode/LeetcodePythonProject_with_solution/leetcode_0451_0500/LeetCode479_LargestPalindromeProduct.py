'''
Created on Nov 19, 2017

@author: MT
'''
class Solution(object):
    ___ largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n == 1: return 9
        upperBound = 10**n-1
        lowerBound = upperBound//10
        maxNum = upperBound*upperBound
        firstHalf = maxNum//(10**n)
        palindromeFound = False
        palindrome = 0
        while not palindromeFound:
            palindrome = self.createPalindrome(firstHalf)
            for i in range(upperBound, lowerBound, -1):
                __ palindrome//i > maxNum or i*i < palindrome:
                    break
                __ palindrome % i == 0:
                    palindromeFound = True
                    break
            firstHalf -= 1
        return int(palindrome%1337)
    
    ___ createPalindrome(self, num):
        s = str(num)+str(num)[::-1]
        return int(s)
    
    ___ test(self):
        testCases = [
            1,
            2,
            3,
            4,
            5,
            6,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.largestPalindrome(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
