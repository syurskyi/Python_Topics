class Solution:
    ___ maxNumber(self, a, b, k):
        """
        :type a: list[int]
        :type b: list[int]
        :type k: int, k <= m + n
        :rtype: list[int]
        """
        ans    # list

        ___ size __ r..(
            max(0, k - l..(a)),
            m..(k, l..(b)) + 1
        ):
            res = self.merge(
                self.get_max(a, k - size),
                self.get_max(b, size)
            )
            ans = max(ans, res)

        r.. ans

    ___ get_max(self, a, size):
        res    # list
        n = l..(a)

        ___ i __ r..(n):
            while (
                res and
                l..(res) + n - i > size and
                res[-1] < a[i]
            ):
                res.pop()

            __ l..(res) < size:
                res.a..(a[i])

        r.. res

    ___ merge(self, a, b):
        r.. [
            max(a, b).pop(0)
            ___ _ __ r..(l..(a) + l..(b))
        ]
