"""
>>> gotcha = []
>>> for _in, _out in (
...     (0, 1), (1, 1),
...     (2, 2), (3, 4),
...     (4, 8), (5, 16),
...     (6, 32), (7, 63),
...     (8, 125), (9, 248),
...
...     res = find_ways_in_board_game(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


___ find_ways_in_board_game(n
    __ not n or n < 2:
        r_ 1

    dp = [0] * (n + 1)
    dp[0] = 1

    ___ i __ range(1, min(n + 1, 6)):
        ___ j __ range(i
            dp[i] += dp[j]

    ___ i __ range(6, n + 1
        dp[i] = su.((
            dp[i - 1],
            dp[i - 2],
            dp[i - 3],
            dp[i - 4],
            dp[i - 5],
            dp[i - 6],
        ))

    r_ dp[n]
