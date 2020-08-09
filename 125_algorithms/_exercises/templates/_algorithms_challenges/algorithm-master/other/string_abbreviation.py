"""
This problem should be discussed, and there might be 3 ways to solve
REF: http://www.1point3acres.com/bbs/thread-218909-1-1.html

1. add specific char to separate. '@'
2. encode number anyway
3. cheating, like '1aaaaa' -> '1a4xa'


>>> CASE = (
...     ('ff', 'ff'),
...     ('fff', 'fff'),
...     ('ffff', '4xf'),
...     ('1xt', '1x1xt'),
...     ('5xt', '1x5xt'),
...     ('1aaaaa', '1x15xa'),
...     ('3aaaaa', '1x35xa'),
...     ('123aaaa', '1x11x21x34xa'),
...     ('aaabbbbcccc', 'aaa4xb4xc'),
... )

>>> all(decode(encode(inpt)) == inpt for inpt, _ in CASE)
True
>>> all(encode(inpt) == oupt for inpt, oupt in CASE)
True
>>> all(decode(oupt) == inpt for inpt, oupt in CASE)
True
"""


___ encode(s
    """
    :type s: str
    :rtype: str
    """
    __ not s:
        r_ ''

    res = []
    cnt = 1
    char = s[0]

    for i in range(1, le.(s)):
        __ s[i] __ s[i - 1]:
            cnt += 1
            continue

        # s[i] != s[i - 1]
        __ char.isdigit() or cnt > 3:
            res.append(str(cnt))
            res.append('x')
            res.append(char)
        ____
            res.append(char * cnt)

        cnt = 1
        char = s[i]

    __ char.isdigit() or cnt > 3:
        res.append(str(cnt))
        res.append('x')
        res.append(char)
    ____
        res.append(char * cnt)

    r_ ''.join(res)


___ decode(s
    """
    :type s: str
    :rtype: str
    """
    __ not s:
        r_ ''

    res = []
    i = 0
    n = le.(s)

    w___ i < n:
        is_digit = s[i].isdigit()

        __ is_digit and i + 2 >= n:
            r_ ''

        __ is_digit:
            res.append(int(s[i]) * s[i + 2])
            i += 3
        ____
            res.append(s[i])
            i += 1

    r_ ''.join(res)
