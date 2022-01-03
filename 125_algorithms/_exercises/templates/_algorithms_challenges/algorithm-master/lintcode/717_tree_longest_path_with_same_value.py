"""
REF: https://blog.csdn.net/zhaohengchuan/article/details/78833501
"""


c_ Solution:
    ___ LongestPathWithSameValue(self, a, e):
        """
        :type a: list[int]
        :type e: list[int]
        :rtype: int
        """
        __ n.. a o. l..(a) <= 1:
            r.. 0

        neibs = [[] ___ _ __ r..(l..(a) + 1)]  # neighbors

        # to build the node connection
        ___ i __ r..(0, l..(e), 2):
            neibs[e[i]].a..(e[i + 1])
            neibs[e[i + 1]].a..(e[i])

        ans = 0
        res = dfs(0, 1, a, neibs)

        r.. max(ans, res)

    ___ dfs(self, root, curr, a, neibs):
        tmp    # list

        ___ neib __ neibs[curr]:
            # ignore if the neib is curr's parent
            __ neib __ root:
                continue

            res = dfs(curr, neib, a, neibs)

            # incr the res and append to tmp
            # if both `neib` and `curr` have same value
            __ a[neib - 1] __ a[curr - 1]:
                tmp.a..(res + 1)

        # to prevent len(tmp) == 0
        tmp.extend((0, 0))
        tmp.s..(r.._T..

        ans = max(ans, tmp[0] + tmp[1])

        r.. tmp[0]
