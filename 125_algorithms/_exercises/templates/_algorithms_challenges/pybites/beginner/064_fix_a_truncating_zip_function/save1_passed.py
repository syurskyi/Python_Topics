_______ itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.s..
locations = 'DE ES AUS NL BR US'.s..
confirmed = [False, True, True, False, True]


___ get_attendees():
    attendee_list = l..(itertools.zip_longest(
        names, locations, confirmed, fillvalue='-'))
    ___ entry __ attendee_list:
        print(entry)


__ __name__ __ '__main__':
    get_attendees()