c_ Solution:
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
            res = merge(
                get_max(a, k - size),
                get_max(b, size)
            )
            ans = max(ans, res)

        r.. ans

    ___ get_max(self, a, size):
        res    # list
        n = l..(a)

        ___ i __ r..(n):
            w.... (
                res a..
                l..(res) + n - i > size a..
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
