____ functools _______ singledispatch


@singledispatch
___ count_down(data_type):
    d = ''
    try:
        __ l..(data_type) != 4:
            r.. ValueError
        ___ i __ data_type:
            d += f'{i}'
    except T..:
        r.. ValueError
    ___ i __ r..(4, 0, -1):
        print(d[:i])


@count_down.register(i..)
___ _(data_type):
    w.... data_type > 0:
        print(data_type)
        data_type //= 10


@count_down.register(float)
___ _(data_type: float):
    s = s..(data_type)
    w.... s != '':
        print(s)
        s = s[:-1]
