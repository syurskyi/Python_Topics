from collections import defaultdict, Counter
from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
__ not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    ___ _load_data(self, data) -> list:
        with open(data) as csv_file:
            csv_dict = [row for row in DictReader(csv_file)]
        return csv_dict


    ___ __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        self.unique_bites_accessed = len(set([row["bite"] for row in self.rows]))
        return self.unique_bites_accessed

    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        self.unique_bites_resolved = len(set([row["bite"] for row in self.rows __ row["completed"] == "True"]))
        return self.unique_bites_resolved

    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        self.unique_users = len(set([row["user"] for row in self.rows]))
        return self.unique_users

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        self.bite_resolved_counter = defaultdict(int)
        for row in self.rows:
            __ row["completed"] == "True":
                self.bite_resolved_counter[row["user"]] += 1
        return len([key for key, value in self.bite_resolved_counter.items() __ value >= 1])

    @property
    ___ top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        self.popular_bite = defaultdict(int)
        for row in self.rows:
            self.popular_bite[row["bite"]] += 1
        return max(self.popular_bite, key=self.popular_bite.get)

    @property
    ___ top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        self.top_user = Counter([row["user"] for row in self.rows __ row["completed"] == "True"])
        return self.top_user.most_common()[0][0]


# if __name__ == "__main__":
#     test = BiteStats()
#     print(test.top_user_by_bites_completed)
