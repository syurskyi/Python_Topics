class Solution:
    ___ maxNumber(self, a, b, k
        """
        :type a: list[int]
        :type b: list[int]
        :type k: int, k <= m + n
        :rtype: list[int]
        """
        ans = []

        ___ size in range(
            max(0, k - le.(a)),
            min(k, le.(b)) + 1

            res = self.merge(
                self.get_max(a, k - size),
                self.get_max(b, size)
            )
            ans = max(ans, res)

        r_ ans

    ___ get_max(self, a, size
        res = []
        n = le.(a)

        ___ i in range(n
            w___ (
                res and
                le.(res) + n - i > size and
                res[-1] < a[i]

                res.p..

            __ le.(res) < size:
                res.append(a[i])

        r_ res

    ___ merge(self, a, b
        r_ [
            max(a, b).pop(0)
            ___ _ in range(le.(a) + le.(b))
        ]
