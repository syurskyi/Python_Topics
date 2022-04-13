MSG 'Hey {}, there are more people with your birthday!'


c_ BirthdayDict(d..
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__  name, birthday
        bday birthday.month, birthday.day

        __ a__([(v.month, v.day) __ bday ___ v __ v..
            print(MSG.f..(name

        update({name: birthday})
