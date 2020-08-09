"""
>>> gotcha = []
>>> for _in, _out in (
...     ((4, 2), 2),
...     ((9, 3), 2.08),
...     ((7, 3), 1.913),
...     ((11, 4), 1.821),
...
...     res = root(*_in)
...     valid = abs(res - _out) < 0.001
...     if not valid: print(_in, res)
...     gotcha.append(valid)
>>> bool(gotcha) and all(gotcha)
True
"""


___ root(x, n
    __ not x or x in (0, 1
        r_ x

    left = 0
    right = max(1, x)

    w___ right - left > 1e-4:
        mid = (left + right) / 2.0
        product = get_product(mid, n)

        __ product < x:
            left = mid
        ____ product > x:
            right = mid
        ____
            r_ mid

    r_ (left + right) / 2.0


___ get_product(x, n
    res = 1

    ___ _ in range(n
        res *= x

    r_ res
