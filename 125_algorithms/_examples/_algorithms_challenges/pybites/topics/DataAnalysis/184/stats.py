from collections import Counter
from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        return [line for line in DictReader(open(data))]  # start here

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return (len(set(dic.get('bite') for dic in self.rows)))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return (len(set(dic.get('bite') for dic in self.rows if dic.get('completed') == 'True')))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return (len(set(dic.get('user') for dic in self.rows)))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return (len(set(dic.get('user') for dic in self.rows if dic.get('completed') == 'True')))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        #most_click = Counter(dic['bite'] for dic in newlist)
        return Counter(dic['bite'] for dic in self.rows).most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        return Counter( dic['user'] for dic in newlist if dic.get('completed') == 'True').most_common(1)[0][0]

new_list = DictReader(open(DATA))
print(new_list.fieldnames)
print(new_list.reader)

newlist = [line for line in new_list]
print(len(newlist))

print(len(set(dic.get('bite') for dic in newlist)))

click_count = Counter( dic['bite'] for dic in newlist)
print(click_count.most_common(1)[0][0])

active_user = Counter( dic['user'] for dic in newlist if dic.get('completed') == 'True')
print(active_user.most_common(1)[0][0])
