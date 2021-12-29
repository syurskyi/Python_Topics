MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        bday = birthday.month, birthday.day

        if any([(v.month, v.day) == bday for v in self.values()]):
            print(MSG.format(name))

        self.update({name: birthday})
