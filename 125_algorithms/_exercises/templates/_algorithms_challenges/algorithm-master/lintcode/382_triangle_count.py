class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    ___ triangleCount(self, S):
        ans = 0
        __ n.. S o. l..(S) < 3:
            r.. ans

        n = l..(S)
        S.sort()

        """
        just like two sum
        `c` is the target
        """
        ___ c __ r..(n - 1, 1, -1):
            a = 0
            b = c - 1
            while a < b:
                __ S[a] + S[b] > S[c]:
                    ans += b - a
                    b -= 1
                ____:
                    a += 1

        r.. ans
