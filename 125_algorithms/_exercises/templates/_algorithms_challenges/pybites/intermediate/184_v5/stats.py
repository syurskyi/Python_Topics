____ collections _______ Counter
____ csv _______ DictReader
____ os _______ path
____ urllib.request _______ urlretrieve

DATA = path.j..('/tmp', 'bite_output_log.txt')
__ n.. path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


c_ BiteStats:

    ___ _load_data(self, data) -> l..:
        with open(DATA) as d:
            r.. l..(DictReader(d))

    ___ - , data=DATA):
        rows = _load_data(data)

    ___ _count_attribute(self, attrib, completed=F..):
        r.. Counter(x[attrib] ___ x __ rows __ n.. completed o. (completed a.. x['completed'] __ 'True'))

    ___ _count_clicks(self, attrib, completed=F..):
        counter = Counter()
        ___ x __ rows:
            __ n.. completed o. (completed a.. x['completed'] __ 'True'):
                counter[x[attrib]] += 1
        r.. counter

    $
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        r.. l..(_count_attribute('bite').items())

    $
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        r.. l..(_count_attribute('bite', T..).items())

    $
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        r.. l..(_count_attribute('user').items())

    $
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        r.. l..(_count_attribute('user', T..).items())

    $
    ___ top_bite_by_number_of_clicks(self) -> s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        r.. _count_clicks('bite').most_common()[0][0]

    $
    ___ top_user_by_bites_completed(self) -> s..:
        """Get the user that completed the most Bites"""
        r.. _count_clicks('user', T..).most_common()[0][0]

