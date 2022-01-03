____ csv _______ DictReader
_______ os
____ urllib.request _______ urlretrieve
____ collections _______ Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.j..(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
__ n.. os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


c_ BiteStats:

    ___ _load_data(self, data) -> l..:
        with open(DATA) as f:
            r.. l..(DictReader(f))

    ___ - , data=DATA):
        rows = _load_data(data)

    $
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        r.. l..({bite['bite'] ___ bite __ rows})

    $
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        r.. l..({bite['bite'] ___ bite __ rows
                    __ bite['completed'] __ 'True'})

    $
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        r.. l..({bite['user'] ___ bite __ rows})

    $
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        r.. l..({bite['user'] ___ bite __ rows
                    __ bite['completed'] __ 'True'})

    $
    ___ top_bite_by_number_of_clicks(self) -> s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        counts = Counter([bite['bite'] ___ bite __ rows])
        r.. counts.most_common(1)[0][0]

    $
    ___ top_user_by_bites_completed(self) -> s..:
        """Get the user that completed the most Bites"""
        counts = Counter([bite['user'] ___ bite __ rows
                         __ bite['completed'] __ 'True'])
        r.. counts.most_common(1)[0][0]
