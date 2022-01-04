____ i.. _______ zip_longest

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.s..
locations = 'DE ES AUS NL BR US'.s..
confirmed = [F.., T.., T.., F.., T..]


___ get_attendees
    ___ participant __ zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


__ __name__ __ '__main__':
    get_attendees()