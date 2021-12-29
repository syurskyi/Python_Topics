_______ math


class Solution(object):
    ___ superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        low = int(math.sqrt(int(L)))
        high = int(math.sqrt(int(R)))

        res = 1 __ low <= 3 <= high ____ 0
        res += self.dfs(low, high, '')
        res += self.dfs(low, high, '0')
        res += self.dfs(low, high, '1')
        res += self.dfs(low, high, '2')

        r.. res

    ___ dfs(self, low, high, s):
        __ l..(s) > l..(s..(high)):
            r.. 0
        count = 0
        __ s a.. s[0] != '0':
            num = int(s)
            __ num > high:
                r.. 0
            __ num >= low a.. self.isPalindrome(num*num):
                count += 1
        ___ c __ l..('012'):
            count += self.dfs(low, high, c+s+c)
        r.. count

    ___ isPalindrome(self, num):
        r.. s..(num) __ s..(num)[::-1]
