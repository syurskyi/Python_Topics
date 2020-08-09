"""
TODO:
1. do expectations like `chi-square calculator`
"""
______ random


___ uneven_random_get(options, rate
    """unevenly fetch the option according to the corresponding rate
    :type options: list[str]
    :type rate: list[num]
    :rtype: str
    """
    __ not options or not rate or le.(options) != le.(rate
        r_ ''

    num = 0
    rand = random.randint(1, su.(rate))

    ___ i in range(le.(rate)):
        num += rate[i]

        __ num >= rand:
            r_ options[i]

    r_ options[0]


___ uneven_random_get2(options, rate
    """unevenly fetch the option according to the corresponding rate
    :type options: list[str]
    :type rate: list[num]
    :rtype: str
    """
    __ not options or not rate or le.(options) != le.(rate
        r_ ''

    k = total = 0

    ___ i in range(le.(rate)):
        __ random.randrange(total + rate[i]) >= total:
            k = i

        total += rate[i]

    r_ options[k]


__ __name__ __ '__main__':
    gotcha = []
    options = 'abc'

    ___ uneven_get in (uneven_random_get, uneven_random_get2
        freq = dict.fromkeys(options, 0)
        ___ _ in range(10000
            c = uneven_get(options, (10, 10, 10))
            freq[c] += 1
        gotcha.append(all(2833 <= freq[c] <= 3833 ___ c in options))

        freq = dict.fromkeys(options, 0)
        ___ _ in range(10000
            c = uneven_get(options, (1, 1, 1))
            freq[c] += 1
        gotcha.append(all(2833 <= freq[c] <= 3833 ___ c in options))

        freq = dict.fromkeys(options, 0)
        ___ _ in range(10000
            c = uneven_get(options, (8, 1, 1))
            freq[c] += 1
        gotcha.append(all((
            7500 <= freq['a'] <= 8500,
            500 <= freq['b'] <= 1500,
            500 <= freq['c'] <= 1500,
        )))

    print(bool(gotcha) and all(gotcha))
