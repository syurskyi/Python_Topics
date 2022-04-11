"""
it's very similar with `next permutation`
just a `next combination`

1. `digits` save unique num and in order
2. `ids` record current used num
3. keep doing plus one and check valid

>>> gotcha = []
>>> s = Solution()
>>> for _in, _out in (
...     ('19:34', '19:39'), ('23:59', '22:22'),
...     ('22:22', '22:22'), ('24:24', ''),
...     ('23:23', '23:32'), ('12:34', '12:41'),
...     ('00:00', '00:00'), ('01:32', '01:33'),
... ):
...     res = s.nextClosestTime(_in)
...     if res != _out: print('in: {}, out: {}, exp: {}'.format(_in, res, _out))
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


c_ Solution:
    ___ nextClosestTime  t__
        """
        :type time: str
        :rtype: str
        """
        __ n.. (
            t__ a.. l..(t__) __ 5 a.. t__[2] __ ':' a..
            0 <_ i..(t__[:2]) < 24 a.. 0 <_ i..(t__[3:]) < 60

            r.. ''

        times = [i..(t) ___ t __ t__ __ t != ':'
        d..    # list

        ___ a __ s..(times
            __ d.. a.. a __ d..[-1]:
                _____

            d...a..(a)

        ids = [d...i.. t) ___ t __ times]
        ids[-1] += 1

        w.... n.. is_valid(ids, d..
            ids[-1] += 1

        h = d..[ids[0]] * 10 + d..[ids[1]]
        m = d..[ids[2]] * 10 + d..[ids[3]]

        r.. '{}:{}'.f..(
            '0' + s..(h) __ h < 10 ____ s..(h),
            '0' + s..(m) __ m < 10 ____ s..(m)
        )

    ___ is_valid  ids, d..
        n = l..(d..)
        carry = 0
        i = l..(ids) - 1

        w.... i >_ 0:
            carry += ids[i]
            ids[i] = carry % n
            carry = carry // n
            i -_ 1

        __ carry:
            ids |  = [0] * l..(ids)
            r.. T..

        h = d..[ids[0]] * 10 + d..[ids[1]]
        m = d..[ids[2]] * 10 + d..[ids[3]]

        __ 0 <_ h < 24 a.. 0 <_ m < 60:
            r.. T..

        r.. F..
