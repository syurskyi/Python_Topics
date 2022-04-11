MSG 'Hey {}, there are more people with your birthday!'


c_ BirthdayDict(d..
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__  name, birthday
        
        ___ key, value __ d...items
            __ birthday.month __ value.month a.. birthday.day __ value.day:
                print(MSG.f..(name

        d...__setitem__  name, birthday)


# bd = BirthdayDict()
# bd['bob'] = date(1987, 6, 15)
# bd['tim'] = date(1984, 7, 15)
# bd['mary'] = date(1987, 6, 15)
# bd['sara'] = date(1987, 6, 14)
# bd['mike'] = date(1981, 7, 15)