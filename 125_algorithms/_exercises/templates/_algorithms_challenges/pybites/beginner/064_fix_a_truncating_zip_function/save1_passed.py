import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


___ get_attendees():
    attendee_list = list(itertools.zip_longest(
        names, locations, confirmed, fillvalue='-'))
    for entry in attendee_list:
        print(entry)


__ __name__ == '__main__':
    get_attendees()