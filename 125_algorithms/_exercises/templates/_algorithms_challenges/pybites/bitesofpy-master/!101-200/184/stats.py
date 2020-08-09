from collections ______ Counter
from csv ______ DictReader
from os ______ path
from urllib.request ______ urlretrieve

DATA = path.join('/tmp', 'bite_output_log.txt')
__ not path.isfile(DATA
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    ___ _load_data(self, data) -> list:
        with open(DATA) as d:
            r_ list(DictReader(d))

    ___ __init__(self, data=DATA
        self.rows = self._load_data(data)

    ___ _count_attribute(self, attrib, completed=False
        r_ Counter(x[attrib] for x in self.rows __ not completed or (completed and x['completed'] __ 'True'))

    ___ _count_clicks(self, attrib, completed=False
        counter = Counter()
        for x in self.rows:
            __ not completed or (completed and x['completed'] __ 'True'
                counter[x[attrib]] += 1
        r_ counter

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        r_ le.(self._count_attribute('bite').items())

    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        r_ le.(self._count_attribute('bite', True).items())

    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        r_ le.(self._count_attribute('user').items())

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        r_ le.(self._count_attribute('user', True).items())

    @property
    ___ top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        r_ self._count_clicks('bite').most_common()[0][0]

    @property
    ___ top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        r_ self._count_clicks('user', True).most_common()[0][0]

