"""
Main Concept:

1. start from 1 => `ans = [1]`
2. use `i2, i3, i5` to record current used in `ans`
3. if the candidates is not ahead `ans[-1]`, move forward
4. append the minimum candidate to `ans`
"""


class Solution:
    ___ nthUglyNumber(self, n
        """
        :type n: int
        :rtype: int
        """
        __ not n:
            r_ 0

        ans = [1]
        i2 = i3 = i5 = 0

        for _ in range(1, n
            w___ ans[i2] * 2 <= ans[-1]:
                i2 += 1
            w___ ans[i3] * 3 <= ans[-1]:
                i3 += 1
            w___ ans[i5] * 5 <= ans[-1]:
                i5 += 1

            ans.append(min((
                ans[i2] * 2,
                ans[i3] * 3,
                ans[i5] * 5,
            )))

        r_ ans[-1]
