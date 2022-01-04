'''
Created on Nov 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n __ 1: r.. 9
        upperBound = 10**n-1
        lowerBound = upperBound//10
        maxNum = upperBound*upperBound
        firstHalf = maxNum//(10**n)
        palindromeFound = F..
        palindrome = 0
        w.... n.. palindromeFound:
            palindrome = createPalindrome(firstHalf)
            ___ i __ r..(upperBound, lowerBound, -1):
                __ palindrome//i > maxNum o. i*i < palindrome:
                    break
                __ palindrome % i __ 0:
                    palindromeFound = T..
                    break
            firstHalf -= 1
        r.. i..(palindrome%1337)
    
    ___ createPalindrome(self, num):
        s = s..(num)+s..(num)[::-1]
        r.. i..(s)
    
    ___ test
        testCases = [
            1,
            2,
            3,
            4,
            5,
            6,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = largestPalindrome(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
