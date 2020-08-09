______ ma__


class Solution(object
    ___ superpalindromesInRange(self, L, R
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        low = int(ma__.sqrt(int(L)))
        high = int(ma__.sqrt(int(R)))

        res = 1 __ low <= 3 <= high else 0
        res += self.dfs(low, high, '')
        res += self.dfs(low, high, '0')
        res += self.dfs(low, high, '1')
        res += self.dfs(low, high, '2')

        r_ res

    ___ dfs(self, low, high, s
        __ le.(s) > le.(str(high)):
            r_ 0
        count = 0
        __ s and s[0] != '0':
            num = int(s)
            __ num > high:
                r_ 0
            __ num >= low and self.isPalindrome(num*num
                count += 1
        for c in list('012'
            count += self.dfs(low, high, c+s+c)
        r_ count

    ___ isPalindrome(self, num
        r_ str(num) __ str(num)[::-1]
