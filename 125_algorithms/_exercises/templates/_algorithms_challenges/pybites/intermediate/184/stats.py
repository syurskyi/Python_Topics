____ collections _______ defaultdict, Counter
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
        with open(data) as csv_file:
            csv_dict = [row ___ row __ DictReader(csv_file)]
        r.. csv_dict


    ___ __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        self.unique_bites_accessed = l..(set([row["bite"] ___ row __ self.rows]))
        r.. self.unique_bites_accessed

    @property
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        self.unique_bites_resolved = l..(set([row["bite"] ___ row __ self.rows __ row["completed"] __ "True"]))
        r.. self.unique_bites_resolved

    @property
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        self.unique_users = l..(set([row["user"] ___ row __ self.rows]))
        r.. self.unique_users

    @property
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        self.bite_resolved_counter = defaultdict(int)
        ___ row __ self.rows:
            __ row["completed"] __ "True":
                self.bite_resolved_counter[row["user"]] += 1
        r.. l..([key ___ key, value __ self.bite_resolved_counter.items() __ value >= 1])

    @property
    ___ top_bite_by_number_of_clicks(self) -> s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        self.popular_bite = defaultdict(int)
        ___ row __ self.rows:
            self.popular_bite[row["bite"]] += 1
        r.. max(self.popular_bite, key=self.popular_bite.get)

    @property
    ___ top_user_by_bites_completed(self) -> s..:
        """Get the user that completed the most Bites"""
        self.top_user = Counter([row["user"] ___ row __ self.rows __ row["completed"] __ "True"])
        r.. self.top_user.most_common()[0][0]


# if __name__ == "__main__":
#     test = BiteStats()
#     print(test.top_user_by_bites_completed)
