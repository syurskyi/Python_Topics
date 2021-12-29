____ functools _______ singledispatch


@singledispatch
___ count_down(data_type):
    d = ''
    try:
        __ l..(data_type) != 4:
            raise ValueError
        ___ i __ data_type:
            d += f'{i}'
    except TypeError:
        raise ValueError
    ___ i __ r..(4, 0, -1):
        print(d[:i])


@count_down.register(int)
___ _(data_type):
    while data_type > 0:
        print(data_type)
        data_type //= 10


@count_down.register(float)
___ _(data_type: float):
    s = str(data_type)
    while s != '':
        print(s)
        s = s[:-1]
