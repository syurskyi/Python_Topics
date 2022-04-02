c_ Solution:
    ___ reverse  x
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        __ n.. x:
            r.. ans

        INT_MAX = 0x7FFFFFFF
        _x = x __ x > 0 ____ -x

        w.... _x:
            ans = ans * 10 + _x % 10
            _x //= 10

        __ ans >= INT_MAX:
            r.. 0

        r.. ans __ x > 0 ____ -ans
