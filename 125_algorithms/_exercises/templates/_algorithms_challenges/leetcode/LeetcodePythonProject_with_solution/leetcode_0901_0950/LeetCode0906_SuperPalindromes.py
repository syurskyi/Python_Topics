import math


class Solution(object):
    ___ superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        low = int(math.sqrt(int(L)))
        high = int(math.sqrt(int(R)))

        res = 1 __ low <= 3 <= high else 0
        res += self.dfs(low, high, '')
        res += self.dfs(low, high, '0')
        res += self.dfs(low, high, '1')
        res += self.dfs(low, high, '2')

        return res

    ___ dfs(self, low, high, s):
        __ len(s) > len(str(high)):
            return 0
        count = 0
        __ s and s[0] != '0':
            num = int(s)
            __ num > high:
                return 0
            __ num >= low and self.isPalindrome(num*num):
                count += 1
        for c in list('012'):
            count += self.dfs(low, high, c+s+c)
        return count

    ___ isPalindrome(self, num):
        return str(num) == str(num)[::-1]
