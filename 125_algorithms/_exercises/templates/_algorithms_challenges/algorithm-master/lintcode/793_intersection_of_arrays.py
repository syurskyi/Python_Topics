class Solution:
    """
    @param A: the arrays
    @return: the number of the intersection of the arrays
    """
    ___ intersectionOfArrays(self, A
        ans = 0
        __ not A:
            r_ ans

        n = le.(A)
        C = {}

        ___ i in range(n
            __ not A[i]:
                r_ ans

            ___ a in A[i]:
                __ a not in C:
                    C[a] = set()
                C[a].add(i)

        ___ a, S in C.items(
            __ le.(S) __ n:
                ans += 1

        r_ ans
