____ c.. _______ C..
____ csv _______ DictReader
____ __ _______ p..
____ u__.r.. _______ u..

DATA = p...j..('/tmp', 'bite_output_log.txt')
__ n.. p...isfile(DATA
    u..('https://bit.ly/2HoFZBd', DATA)


c_ BiteStats:

    ___ _load_data  data) __ l..:
        w__ o.. DATA) __ d:
            r.. l..(DictReader(d))

    ___ - , data=DATA
        rows = _load_data(data)

    ___ _count_attribute  attrib, completed=F..
        r.. C..(x[attrib] ___ x __ rows __ n.. completed o. (completed a.. x 'completed'  __ 'True'))

    ___ _count_clicks  attrib, completed=F..
        counter = C..()
        ___ x __ rows:
            __ n.. completed o. (completed a.. x 'completed'  __ 'True'
                counter[x[attrib]] += 1
        r.. counter

    $
    ___ number_bites_accessed(self) __ i..:
        """Get the number of unique Bites accessed"""
        r.. l..(_count_attribute('bite').i..

    $
    ___ number_bites_resolved(self) __ i..:
        """Get the number of unique Bites resolved (completed=True)"""
        r.. l..(_count_attribute('bite', T..).i..

    $
    ___ number_users_active(self) __ i..:
        """Get the number of unique users in the data set"""
        r.. l..(_count_attribute('user').i..

    $
    ___ number_users_solving_bites(self) __ i..:
        """Get the number of unique users that resolved
           one or more Bites"""
        r.. l..(_count_attribute('user', T..).i..

    $
    ___ top_bite_by_number_of_clicks(self) __ s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        r.. _count_clicks('bite').most_common()[0][0]

    $
    ___ top_user_by_bites_completed(self) __ s..:
        """Get the user that completed the most Bites"""
        r.. _count_clicks('user', T..).most_common()[0][0]

