MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(d..):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__(self, name, birthday):
        
        ___ key, value __ d...items(self):
            __ birthday.month __ value.month and birthday.day __ value.day:
                print(MSG.format(name))

        d...__setitem__(self, name, birthday)


# bd = BirthdayDict()
# bd['bob'] = date(1987, 6, 15)
# bd['tim'] = date(1984, 7, 15)
# bd['mary'] = date(1987, 6, 15)
# bd['sara'] = date(1987, 6, 14)
# bd['mike'] = date(1981, 7, 15)