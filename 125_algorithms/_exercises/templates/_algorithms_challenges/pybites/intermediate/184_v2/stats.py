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


        with open(data,'r') as f:
            csv_reader = DictReader(f,delimiter=',')

            for row in csv_reader:
                yield row






    ___ __init__(self, data=DATA):
        self.rows = list(self._load_data(data))

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        bites = set()
        for row in self.rows:
            bites.add(row['bite'])

        return len(bites)





    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        completed = set()
        for row in self.rows:
            __ row['completed'] == 'True':
                completed.add(row['bite'])
        return len(completed)



    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        users = set()
        for row in self.rows:
            users.add(row['user'])

        return len(users)
            

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        users = set()

        for row in filter(lambda row: row['completed'] == 'True',self.rows):
            users.add(row['user'])

        return len(users)



    @property
    ___ top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""


        return Counter(row['bite'] for row in self.rows).most_common(1)[0][0]

    @property
    ___ top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""

        return Counter(row['user'] for row in filter(lambda row: row['completed'] == 'True',self.rows)).most_common(1)[0][0]



__ __name__ == "__main__":

    l = BiteStats(DATA)

    print(list(l.rows))
    



