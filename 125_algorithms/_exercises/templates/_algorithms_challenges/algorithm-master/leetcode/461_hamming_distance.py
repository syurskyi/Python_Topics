c_ Solution:
    ___ hammingDistance  x, y
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n x ^ y
        ans 0

        __ n.. n:
            r.. ans

        w.... n != 0:
            n n & (n - 1)
            ans += 1

        r.. ans
