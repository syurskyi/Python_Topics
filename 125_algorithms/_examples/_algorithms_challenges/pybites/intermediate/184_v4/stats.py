from csv import DictReader
import os
from u__.r.. import u..
from collections import Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    u..(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(DATA) as f:
            return list(DictReader(f))

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({bite['bite'] for bite in self.rows})

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({bite['bite'] for bite in self.rows
                    if bite['completed'] == 'True'})

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({bite['user'] for bite in self.rows})

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len({bite['user'] for bite in self.rows
                    if bite['completed'] == 'True'})

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        counts = Counter([bite['bite'] for bite in self.rows])
        return counts.most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        counts = Counter([bite['user'] for bite in self.rows
                         if bite['completed'] == 'True'])
        return counts.most_common(1)[0][0]
