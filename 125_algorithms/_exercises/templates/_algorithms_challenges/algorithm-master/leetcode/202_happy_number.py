c_ Solution:
    ___ isHappy  n
        """
        :type n: int
        :rtype: bool
        """
        slow square_sum(n)
        fast square_sum(slow)

        w.... slow != fast:
            slow square_sum(slow)
            fast square_sum(
                square_sum(fast)
            )

        r.. T.. __ slow __ 1 ____ F..

    ___ square_sum  a
        res b 0

        w.... a != 0:
            b a % 10
            res += b * b
            a //= 10

        r.. res
