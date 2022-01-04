MSG = 'Hey {}, there are more people with your birthday!'


c_ BirthdayDict(d..):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ - , *args, **kwargs):
        super().__init__()
        update $ $$

    ___ __setitem__(self, name, birthday):
        __ any((birthday.day __ x.day a.. birthday.month __ x.month) ___ (_, x) __ i..:
            print(MSG.f..(name))
        d...__setitem__(self, name, birthday)
