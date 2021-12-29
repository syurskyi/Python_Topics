import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


___ get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


__ __name__ == '__main__':
    get_attendees()