# NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
#          'julian sequeira', 'sandra bullock', 'keanu reeves',
#          'julbob pybites', 'bob belderbos', 'julian sequeira',
#          'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
#
#
# ___ dedup_and_title_case_names names
#     """Should return a list of title cased names,
#        each name appears only once"""
#     non_dup_lst    # list
#     ___ x __ names
#         __ x n.. __ ?
#             ?.a.. ?
#     non_dup_lst  element.t.. ___ ? __ ?
#     r.. non_dup_lst
#
#
# ___ sort_by_surname_desc names
#     """Returns names list sorted desc by surname"""
#     names ? ?
#     ?.s.. k.._l.... x ?.s.. 1
#     r.. ?
#
#
# ___ shortest_first_name names
#     """Returns the shortest first name (str).
#        You can assume there is only one shortest name.
#     """
#     names ? ?
#     first_name  x.s.. 0 ___ ? __ ?
#     shortest_name  m.. ? k.._l..
#     r.. ?

# if __name__ == '__main__':
#     names = dedup_and_title_case_names(NAMES)
#     print(names)
#     names = dedup_and_title_case_names(PY_CONTENT_CREATORS)
#     print(names)
#     sort_by_surname_desc = sort_by_surname_desc(NAMES)
#     print(sort_by_surname_desc)
#     shortest_first_name = shortest_first_name(NAMES)
#     print(shortest_first_name)