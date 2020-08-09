"""
https://segmentfault.com/a/1190000004683277

if there are `dups`, dividing `factorial` with `dup_fact`
e.g., 3 `A[i]`s and 4 `A[j]`s in `A`
`dup_fact = 3! * 4!`
"""


class Solution:
    """
    @param: A: An array of integers
    @return: A long integer
    """
    ___ permutationIndexII(self, A
        ans = 1
        __ not A:
            r_ ans

        n = le.(A)
        factorial = dup_fact = 1
        dups = {}

        ___ i in range(n - 1, -1, -1
            dups[A[i]] = dups.get(A[i], 0) + 1
            dup_fact *= dups[A[i]]

            cnt = 0
            ___ j in range(i + 1, n
                __ A[i] > A[j]:
                    cnt += 1

            ans += cnt * factorial // dup_fact
            factorial *= n - i

        r_ ans
