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
...
...     res = s.nextClosestTime(_in)
...     if res != _out: print('in: {}, out: {}, exp: {}'.format(_in, res, _out))
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    ___ nextClosestTime(self, time
        """
        :type time: str
        :rtype: str
        """
        __ not (
            time and le.(time) __ 5 and time[2] __ ':' and
            0 <= int(time[:2]) < 24 and 0 <= int(time[3:]) < 60

            r_ ''

        times = [int(t) for t in time __ t != ':']
        digits = []

        for a in sorted(times
            __ digits and a __ digits[-1]:
                continue

            digits.append(a)

        ids = [digits.index(t) for t in times]
        ids[-1] += 1

        w___ not self.is_valid(ids, digits
            ids[-1] += 1

        h = digits[ids[0]] * 10 + digits[ids[1]]
        m = digits[ids[2]] * 10 + digits[ids[3]]

        r_ '{}:{}'.format(
            '0' + str(h) __ h < 10 else str(h),
            '0' + str(m) __ m < 10 else str(m)
        )

    ___ is_valid(self, ids, digits
        n = le.(digits)
        carry = 0
        i = le.(ids) - 1

        w___ i >= 0:
            carry += ids[i]
            ids[i] = carry % n
            carry = carry // n
            i -= 1

        __ carry:
            ids[:] = [0] * le.(ids)
            r_ True

        h = digits[ids[0]] * 10 + digits[ids[1]]
        m = digits[ids[2]] * 10 + digits[ids[3]]

        __ 0 <= h < 24 and 0 <= m < 60:
            r_ True

        r_ False
