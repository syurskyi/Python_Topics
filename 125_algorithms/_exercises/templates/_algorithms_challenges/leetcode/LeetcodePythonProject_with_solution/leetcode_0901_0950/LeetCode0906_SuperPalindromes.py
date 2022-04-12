_______ m__


c_ Solution(o..
    ___ superpalindromesInRange  L, R
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        low i..(m__.sqrt(i..(L)))
        high i..(m__.sqrt(i..(R)))

        res 1 __ low <_ 3 <_ high ____ 0
        res += dfs(low, high, '')
        res += dfs(low, high, '0')
        res += dfs(low, high, '1')
        res += dfs(low, high, '2')

        r.. res

    ___ dfs  low, high, s
        __ l..(s) > l..(s..(high:
            r.. 0
        count 0
        __ s a.. s[0] !_ '0':
            num i..(s)
            __ num > high:
                r.. 0
            __ num >_ low a.. isPalindrome(num*num
                count += 1
        ___ c __ l..('012'
            count += dfs(low, high, c+s+c)
        r.. count

    ___ isPalindrome  num
        r.. s..(num) __ s..(num)[::-1]
