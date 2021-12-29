"""
Main Concept:

1. start from 1 => `ans = [1]`
2. use `i2, i3, i5` to record current used in `ans`
3. if the candidates is not ahead `ans[-1]`, move forward
4. append the minimum candidate to `ans`
"""


class Solution:
    ___ nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n.. n:
            r.. 0

        ans = [1]
        i2 = i3 = i5 = 0

        ___ _ __ r..(1, n):
            w.... ans[i2] * 2 <= ans[-1]:
                i2 += 1
            w.... ans[i3] * 3 <= ans[-1]:
                i3 += 1
            w.... ans[i5] * 5 <= ans[-1]:
                i5 += 1

            ans.a..(m..((
                ans[i2] * 2,
                ans[i3] * 3,
                ans[i5] * 5,
            )))

        r.. ans[-1]
