_______ i..

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.s..
locations = 'DE ES AUS NL BR US'.s..
confirmed = [F.., T.., T.., F.., T..]


___ get_attendees
    attendee_list = l..(i...zip_longest(
        names, locations, confirmed, fillvalue='-'))
    ___ entry __ attendee_list:
        print(entry)


__ __name__ __ '__main__':
    get_attendees()