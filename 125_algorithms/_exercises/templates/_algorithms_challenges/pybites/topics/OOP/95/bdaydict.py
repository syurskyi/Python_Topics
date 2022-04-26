____ d__ _______ date


MSG 'Hey {}, there are more people with your birthday!'


c_ BirthdayDict(d..
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ - , $  $$
        update $ $$

    ___ -s  name birthday
        ___ date __ v..
            __ date.month __ birthday.month a.. date.day __ birthday.day:
                print(MSG.f..(name
        update({name: birthday})

bd BirthdayDict()
bd 'khoo'  = date(1968,4,29)
bd 'chuan'  = date(1968,4,26)
bd 'bob'   ? 1987, 6, 15
bd 'tim'   ? 1984, 7, 15
bd 'mary'   ? 1987, 6, 15
bd 'sara'  ? 1987, 6, 14
bd 'mike'  ? 1981, 7, 15

#print(type(bd))