c_ Solution:
    ___ lastRemaining  n
        """
        :type n: int
        :rtype: int
        """
        ans = gap = 1
        turn = 0

        w.... n > 1:
            turn += 1
            n //= 2
            gap *= 2
            delta = gap // 2 + gap * (n - 1)

            __ turn & 1:
                ans += delta
            ____:
                ans -= delta

        r.. ans
