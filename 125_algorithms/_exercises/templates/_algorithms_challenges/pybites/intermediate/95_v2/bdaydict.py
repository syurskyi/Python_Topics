MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(d..):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__(self, name, birthday):
        ___ b __ self.values():
            __ b.month __ birthday.month a.. b.day __ birthday.day:
                print(MSG.f..(name))

        super().__setitem__(name,birthday)


