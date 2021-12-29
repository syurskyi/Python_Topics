MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(d..):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    ___ __setitem__(self, name, birthday):
        bday = birthday.month, birthday.day

        __ any([(v.month, v.day) __ bday ___ v __ self.values()]):
            print(MSG.f..(name))

        self.update({name: birthday})
