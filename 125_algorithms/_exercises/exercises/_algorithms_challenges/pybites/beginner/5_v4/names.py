# ____ pprint _______ pprint
#
# NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
#          'julian sequeira', 'sandra bullock', 'keanu reeves',
#          'julbob pybites', 'bob belderbos', 'julian sequeira',
#          'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
#
#
# ___ dedup_and_title_case_names names
#     """Should return a list of title cased names,
#        each name appears only once"""
#     r.. l.. ? x .t.. ___ ? __ r.. l.. ?
#
#
# ___ sort_by_surname_desc names
#     """Returns names list sorted desc by surname"""
#     names ? ?
#     r.. s.. ? k.._l.... x ?.s.. 1 r.._T..
#
#
# ___ shortest_first_name names
#     """Returns the shortest first name (str).
#        You can assume there is only one shortest name.
#     """
#     names ? ?
#     r.. s.. ? k.._l.... x l.. ?.s.. 0 0 .s.. 0
#
#
# ___ test_dedup_and_title_case_names():
#     names = dedup_and_title_case_names(NAMES)
#     ... names.c.. 'Bob Belderbos') __ 1
#     ... names.c.. 'julian sequeira') __ 0
#     ... names.c.. 'Brad Pitt') __ 1
#     ... l..(names) __ 10
#     ... a..(n.t.. __ names ___ n __ NAMES)
#
#
# # test_dedup_and_title_case_names()
# # pprint(dedup_and_title_case_names(NAMES))
# pprint(sort_by_surname_desc(NAMES))
# pprint(shortest_first_name(NAMES))
