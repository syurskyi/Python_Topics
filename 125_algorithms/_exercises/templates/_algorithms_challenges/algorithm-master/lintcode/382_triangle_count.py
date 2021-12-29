class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    ___ triangleCount(self, S):
        ans = 0
        __ not S or len(S) < 3:
            return ans

        n = len(S)
        S.sort()

        """
        just like two sum
        `c` is the target
        """
        for c in range(n - 1, 1, -1):
            a = 0
            b = c - 1
            while a < b:
                __ S[a] + S[b] > S[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1

        return ans
