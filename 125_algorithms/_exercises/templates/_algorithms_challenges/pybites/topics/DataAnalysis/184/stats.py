____ c.. _______ C..
____ c__ _______ DictReader
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
        r.. [line ___ line __ DictReader(o.. data]  # start here

    ___ - , data=DATA
        rows _load_data(data)

    $
    ___ number_bites_accessed(self) __ i..:
        """Get the number of unique Bites accessed"""
        r.. (l..(s..(dic.g.. 'bite') ___ dic __ rows)))

    $
    ___ number_bites_resolved(self) __ i..:
        """Get the number of unique Bites resolved (completed=True)"""
        r.. (l..(s..(dic.g.. 'bite') ___ dic __ rows __ dic.g.. 'completed') __ 'True')))

    $
    ___ number_users_active(self) __ i..:
        """Get the number of unique users in the data set"""
        r.. (l..(s..(dic.g.. 'user') ___ dic __ rows)))

    $
    ___ number_users_solving_bites(self) __ i..:
        """Get the number of unique users that resolved
           one or more Bites"""
        r.. (l..(s..(dic.g.. 'user') ___ dic __ rows __ dic.g.. 'completed') __ 'True')))

    $
    ___ top_bite_by_number_of_clicks(self) __ s..:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        #most_click = Counter(dic['bite'] for dic in newlist)
        r.. C..(dic 'bite'  ___ dic __ rows).most_common 1 0 0

    $
    ___ top_user_by_bites_completed(self) __ s..:
        """Get the user that completed the most Bites"""
        r.. C..( dic 'user'  ___ dic __ newlist __ dic.g.. 'completed') __ 'True').most_common 1 0 0

new_list DictReader(o.. DATA
print(new_list.fieldnames)
print(new_list.reader)

newlist [line ___ line __ new_list]
print(l..(newlist

print(l..(s..(dic.g.. 'bite') ___ dic __ newlist)))

click_count C..( dic 'bite'  ___ dic __ newlist)
print(click_count.most_common 1 0 0)

active_user C..( dic 'user'  ___ dic __ newlist __ dic.g.. 'completed') __ 'True')
print(active_user.most_common 1 0 0)
