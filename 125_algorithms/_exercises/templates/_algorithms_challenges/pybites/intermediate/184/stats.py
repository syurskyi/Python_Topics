____ c.. _______ d.., C..
____ csv _______ DictReader
_______ __
____ u__.r.. _______ u..

TMP __.g.. TMP  /tmp
LOGS 'bite_output_log.txt'
DATA __.p...j..(TMP, LOGS)
S3 'https://bites-data.s3.us-east-2.amazonaws.com'
__ n.. __.p...i..(DATA
    u.. _*{S3}/{LOGS}', DATA)


c_ BiteStats:

    ___ _load_data  data) __ l..:
        w__ o.. data) __ csv_file:
            csv_dict [row ___ row __ DictReader(csv_file)]
        r.. csv_dict


    ___ - , data=DATA
        rows _load_data(data)

    $
    ___ number_bites_accessed(self) __ i..:
        """Get the number of unique Bites accessed"""
        unique_bites_accessed l..(s..([row["bite"] ___ row __ rows]
        r.. unique_bites_accessed

    $
    ___ number_bites_resolved(self) __ i..:
        """Get the number of unique Bites resolved (completed=True)"""
        unique_bites_resolved l..(s..([row["bite"] ___ row __ rows __ row["completed"] __ "True"]
        r.. unique_bites_resolved

    $
    ___ number_users_active(self) __ i..:
        """Get the number of unique users in the data set"""
        unique_users l..(s..([row["user"] ___ row __ rows]
        r.. unique_users

    $
    ___ number_users_solving_bites(self) __ i..:
        """Get the number of unique users that resolved
           one or more Bites"""
        bite_resolved_counter d..(i..)
        ___ row __ rows:
            __ row["completed"] __ "True":
                bite_resolved_counter[row["user"]] += 1
        r.. l..([key ___ key, value __ bite_resolved_counter.i.. __ value >_ 1])

    $
    ___ top_bite_by_number_of_clicks(self) __ s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        popular_bite d..(i..)
        ___ row __ rows:
            popular_bite[row["bite"]] += 1
        r.. m..(popular_bite, key=popular_bite.get)

    $
    ___ top_user_by_bites_completed(self) __ s..:
        """Get the user that completed the most Bites"""
        top_user C..([row["user"] ___ row __ rows __ row["completed"] __ "True"])
        r.. top_user.m..[0][0]


# if __name__ == "__main__":
#     test = BiteStats()
#     print(test.top_user_by_bites_completed)
