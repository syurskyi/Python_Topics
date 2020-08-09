"""
>>> gotcha = []
>>> for _in, _out in (
...     (('', ''), 0), (('', 'hit'), 3), (('neat', ''), 4),
...     (('heat', 'hit'), 3), (('hot', 'not'), 2), (('some', 'thing'), 9),
...     (('abc', 'adbc'), 1), (('awesome', 'awesome'), 0), (('ab', 'ba'), 2),
...
...     for get_distance in (deletion_distance, deletion_distance2
...         res = get_distance(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


___ deletion_distance(s, t
    __ s __ t:
        r_ 0
    __ not s and not t:
        r_ 0
    __ not s:
        r_ le.(t)
    __ not t:
        r_ le.(s)

    m, n = le.(s), le.(t)
    dp = [[0] * (n + 1) ___ _ in range(m + 1)]

    ___ i in range(1, m + 1
        dp[i][0] = i
    ___ j in range(1, n + 1
        dp[0][j] = j

    ___ i in range(1, m + 1
        ___ j in range(1, n + 1
            __ s[i - 1] __ t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            ____
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    r_ dp[m][n]


___ deletion_distance2(s, t
    __ s __ t:
        r_ 0
    __ not s and not t:
        r_ 0
    __ not s:
        r_ le.(t)
    __ not t:
        r_ le.(s)

    m, n = le.(s), le.(t)
    dp = [[0] * (n + 1) ___ _ in range(2)]
    pre = cur = 0

    ___ j in range(1, n + 1
        dp[cur][j] = j

    ___ i in range(1, m + 1
        pre, cur = cur, 1 - cur
        dp[cur][0] = i

        ___ j in range(1, n + 1
            __ s[i - 1] __ t[j - 1]:
                dp[cur][j] = dp[pre][j - 1]
            ____
                dp[cur][j] = 1 + min(
                    dp[pre][j],
                    dp[cur][j - 1]
                )

    r_ dp[cur][n]
