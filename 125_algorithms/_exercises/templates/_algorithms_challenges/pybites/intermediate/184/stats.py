____ collections _______ defaultdict, Counter
____ csv _______ DictReader
_______ os
____ urllib.request _______ urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.j..(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
__ n.. os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


c_ BiteStats:

    ___ _load_data(self, data) -> l..:
        with open(data) as csv_file:
            csv_dict = [row ___ row __ DictReader(csv_file)]
        r.. csv_dict


    ___ - , data=DATA):
        rows = _load_data(data)

    $
    ___ number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        unique_bites_accessed = l..(set([row["bite"] ___ row __ rows]))
        r.. unique_bites_accessed

    $
    ___ number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        unique_bites_resolved = l..(set([row["bite"] ___ row __ rows __ row["completed"] __ "True"]))
        r.. unique_bites_resolved

    $
    ___ number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        unique_users = l..(set([row["user"] ___ row __ rows]))
        r.. unique_users

    $
    ___ number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        bite_resolved_counter = defaultdict(int)
        ___ row __ rows:
            __ row["completed"] __ "True":
                bite_resolved_counter[row["user"]] += 1
        r.. l..([key ___ key, value __ bite_resolved_counter.i.. __ value >= 1])

    $
    ___ top_bite_by_number_of_clicks(self) -> s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        popular_bite = defaultdict(int)
        ___ row __ rows:
            popular_bite[row["bite"]] += 1
        r.. max(popular_bite, key=popular_bite.get)

    $
    ___ top_user_by_bites_completed(self) -> s..:
        """Get the user that completed the most Bites"""
        top_user = Counter([row["user"] ___ row __ rows __ row["completed"] __ "True"])
        r.. top_user.most_common()[0][0]


# if __name__ == "__main__":
#     test = BiteStats()
#     print(test.top_user_by_bites_completed)
