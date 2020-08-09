class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    ___ triangleCount(self, S
        ans = 0
        __ not S or le.(S) < 3:
            r_ ans

        n = le.(S)
        S.sort()

        """
        just like two sum
        `c` is the target
        """
        ___ c in range(n - 1, 1, -1
            a = 0
            b = c - 1
            w___ a < b:
                __ S[a] + S[b] > S[c]:
                    ans += b - a
                    b -= 1
                ____
                    a += 1

        r_ ans
