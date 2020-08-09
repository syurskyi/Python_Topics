"""
REF: https://blog.csdn.net/zhaohengchuan/article/details/78833501
"""


class Solution:
    ___ LongestPathWithSameValue(self, a, e
        """
        :type a: list[int]
        :type e: list[int]
        :rtype: int
        """
        __ not a or le.(a) <= 1:
            r_ 0

        neibs = [[] for _ in range(le.(a) + 1)]  # neighbors

        # to build the node connection
        for i in range(0, le.(e), 2
            neibs[e[i]].append(e[i + 1])
            neibs[e[i + 1]].append(e[i])

        self.ans = 0
        res = self.dfs(0, 1, a, neibs)

        r_ max(self.ans, res)

    ___ dfs(self, root, curr, a, neibs
        tmp = []

        for neib in neibs[curr]:
            # ignore if the neib is curr's parent
            __ neib __ root:
                continue

            res = self.dfs(curr, neib, a, neibs)

            # incr the res and append to tmp
            # if both `neib` and `curr` have same value
            __ a[neib - 1] __ a[curr - 1]:
                tmp.append(res + 1)

        # to prevent le.(tmp) == 0
        tmp.extend((0, 0))
        tmp.sort(reverse=True)

        self.ans = max(self.ans, tmp[0] + tmp[1])

        r_ tmp[0]
