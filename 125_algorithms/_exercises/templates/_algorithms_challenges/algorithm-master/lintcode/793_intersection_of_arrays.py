class Solution:
    """
    @param A: the arrays
    @return: the number of the intersection of the arrays
    """
    ___ intersectionOfArrays(self, A):
        ans = 0
        __ n.. A:
            r.. ans

        n = l..(A)
        C = {}

        ___ i __ r..(n):
            __ n.. A[i]:
                r.. ans

            ___ a __ A[i]:
                __ a n.. __ C:
                    C[a] = set()
                C[a].add(i)

        ___ a, S __ C.items():
            __ l..(S) __ n:
                ans += 1

        r.. ans
