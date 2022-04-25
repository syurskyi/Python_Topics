MSG 'Hey {}, there are more people with your birthday!'


c_ BirthdayDict(d..
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__  name, birthday
        ___ b __ v..
            __ b.month __ birthday.month a.. b.day __ birthday.day:
                print(MSG.f..(name

        ____.__setitem__(name,birthday)


