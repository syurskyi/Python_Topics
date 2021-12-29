from datetime import date


MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        for date in self.values():
            if date.month == birthday.month and date.day == birthday.day:
                print(MSG.format(name))
        self.update({name: birthday})

bd = BirthdayDict()
bd['khoo'] = date(1968,4,29)
bd['chuan'] = date(1968,4,26)
bd['bob'] = date(1987, 6, 15)
bd['tim'] = date(1984, 7, 15)
bd['mary'] = date(1987, 6, 15)
bd['sara'] = date(1987, 6, 14)
bd['mike'] = date(1981, 7, 15)

#print(type(bd))