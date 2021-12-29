from csv import DictReader
import os
from urllib.request import urlretrieve
from collections import Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
__ not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    ___ _load_data(self, data) -> list:
        with open(DATA) as f:
            return list(DictReader(f))

    ___ __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({bite['bite'] for bite in self.rows})

    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({bite['bite'] for bite in self.rows
                    __ bite['completed'] == 'True'})

    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({bite['user'] for bite in self.rows})

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len({bite['user'] for bite in self.rows
                    __ bite['completed'] == 'True'})

    @property
    ___ top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        counts = Counter([bite['bite'] for bite in self.rows])
        return counts.most_common(1)[0][0]

    @property
    ___ top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        counts = Counter([bite['user'] for bite in self.rows
                         __ bite['completed'] == 'True'])
        return counts.most_common(1)[0][0]
