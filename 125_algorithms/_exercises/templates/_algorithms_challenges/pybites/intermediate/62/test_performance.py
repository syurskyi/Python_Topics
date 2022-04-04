____ s__ _______ ascii_lowercase

____ performance _______ (contains, contains_fast,
                         ordered_list_max, ordered_list_max_fast,
                         list_concat, list_concat_fast,
                         list_inserts, list_inserts_fast,
                         list_creation, list_creation_fast)

alist = l..(r..(1000000
aset = s..(alist)
listofstrings = l..(ascii_lowercase) * 1000


___ test_contains
    t1, res1 = contains(alist, 500)
    t2, res2 = contains_fast(aset, 1000)
    ... res1 __ res2
    ... t1 >= t2


___ test_ordered_max
    t1, res1 = ordered_list_max(alist)
    t2, res2 = ordered_list_max_fast(alist)
    ... res1 __ res2
    ... t1 > t2


___ test_concat
    t1, res1 = list_concat(listofstrings)
    t2, res2 = list_concat_fast(listofstrings)
    ... res1 __ res2
    ... t1 > t2


___ test_list_insert
    t1, res1 = list_inserts(10000)
    t2, res2 = list_inserts_fast(10000)
    ... l..(res1) __ l..(res2)
    ... t1 > t2


___ test_list_creation
    t1, res1 = list_creation(10000)
    t2, res2 = list_creation_fast(10000)
    ... l..(res1) __ l..(res2)
    ... t1 > t2
