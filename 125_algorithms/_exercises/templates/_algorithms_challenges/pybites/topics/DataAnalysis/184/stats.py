____ collections _______ Counter
____ csv _______ DictReader
_______ os
____ urllib.request _______ urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
__ n.. os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    ___ _load_data(self, data) -> l..:
        r.. [line ___ line __ DictReader(open(data))]  # start here

    ___ __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        r.. (l..(set(dic.get('bite') ___ dic __ self.rows)))

    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        r.. (l..(set(dic.get('bite') ___ dic __ self.rows __ dic.get('completed') __ 'True')))

    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        r.. (l..(set(dic.get('user') ___ dic __ self.rows)))

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        r.. (l..(set(dic.get('user') ___ dic __ self.rows __ dic.get('completed') __ 'True')))

    @property
    ___ top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        #most_click = Counter(dic['bite'] for dic in newlist)
        r.. Counter(dic['bite'] ___ dic __ self.rows).most_common(1)[0][0]

    @property
    ___ top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        r.. Counter( dic['user'] ___ dic __ newlist __ dic.get('completed') __ 'True').most_common(1)[0][0]

new_list = DictReader(open(DATA))
print(new_list.fieldnames)
print(new_list.reader)

newlist = [line ___ line __ new_list]
print(l..(newlist))

print(l..(set(dic.get('bite') ___ dic __ newlist)))

click_count = Counter( dic['bite'] ___ dic __ newlist)
print(click_count.most_common(1)[0][0])

active_user = Counter( dic['user'] ___ dic __ newlist __ dic.get('completed') __ 'True')
print(active_user.most_common(1)[0][0])
