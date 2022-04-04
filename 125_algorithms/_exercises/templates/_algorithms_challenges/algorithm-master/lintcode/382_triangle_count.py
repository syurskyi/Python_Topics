c_ Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    ___ triangleCount  S
        ans = 0
        __ n.. S o. l..(S) < 3:
            r.. ans

        n = l..(S)
        S.s..()

        """
        just like two sum
        `c` is the target
        """
        ___ c __ r..(n - 1, 1, -1
            a = 0
            b = c - 1
            w.... a < b:
                __ S[a] + S[b] > S[c]:
                    ans += b - a
                    b -= 1
                ____
                    a += 1

        r.. ans
