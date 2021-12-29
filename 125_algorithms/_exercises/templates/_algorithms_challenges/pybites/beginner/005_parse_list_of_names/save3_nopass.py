NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


___ dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    non_dup_lst    # list
    ___ x __ names:
        __ x n.. __ non_dup_lst:
            non_dup_lst.a..(x)
    non_dup_lst = [element.t.. ___ element __ non_dup_lst]
    r.. non_dup_lst


___ sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=l.... x: x.s.. [1], reverse=False)
    r.. names


___ shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_name = [x.s.. [0] ___ x __ names]
    shortest_name = m..(first_name, key=l..)
    r.. shortest_name