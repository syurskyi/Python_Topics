c_ Solution o..
    # def largestPalindrome(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 9
    #     # https://leetcode.com/problems/largest-palindrome-product/discuss/96297/Java-Solution-using-assumed-max-palindrom
    #     upperBound = 10 ** n - 1
    #     lowerBound = upperBound / 10
    #     maxNum = upperBound * upperBound
    #     firstHalf = maxNum / (10 ** n)
    #     palindromFound = False
    #     palindrom = 0
    #     while not palindromFound:
    #         palindrom = int(str(firstHalf) + str(firstHalf)[::-1])
    #         for i in xrange(upperBound, lowerBound, -1):
    #             if i * i < palindrom:
    #                 break
    #             if palindrom % i == 0:
    #                 palindromFound = True
    #                 break
    #         firstHalf -= 1
    #     return palindrom % 1337

    ___ largestPalindrome  n):
        # https://leetcode.com/problems/largest-palindrome-product/discuss/96305/Python-Solution-Using-Math-In-48ms
        # https://leetcode.com/problems/largest-palindrome-product/discuss/96294/could-any-python-experts-share-their-codes-within-100ms
        __ n __ 1:
            r_ 9
        ___ a __ xrange(2, 9 * 10 ** (n - 1)):
            hi = (10 ** n) - a
            lo = i..(s..(hi)||-1])
            __ a ** 2 - 4 * lo < 0:
                continue
            __ (a ** 2 - 4 * lo) ** .5 __ i..((a ** 2 - 4 * lo) ** .5):
                r_ (lo + 10 ** n * (10 ** n - a)) % 1337
