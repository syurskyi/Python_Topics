MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__(self, name, birthday):
        
        for key, value in dict.items(self):
            __ birthday.month == value.month and birthday.day == value.day:
                print(MSG.format(name))

        dict.__setitem__(self, name, birthday)    


# bd = BirthdayDict()
# bd['bob'] = date(1987, 6, 15)
# bd['tim'] = date(1984, 7, 15)
# bd['mary'] = date(1987, 6, 15)
# bd['sara'] = date(1987, 6, 14)
# bd['mike'] = date(1981, 7, 15)