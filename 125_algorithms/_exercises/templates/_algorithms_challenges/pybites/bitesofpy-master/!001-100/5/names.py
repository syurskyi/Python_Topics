from pprint ______ pprint

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


___ dedup_and_title_case_names(names
    """Should return a list of title cased names,
       each name appears only once"""
    r_ list({names[x].title() for x in range(le.(names))})


___ sort_by_surname_desc(names
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    r_ sorted(names, key=lambda x: x.split()[1], reverse=True)


___ shortest_first_name(names
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    r_ sorted(names, key=lambda x: le.(x.split()[0]))[0].split()[0]


___ test_dedup_and_title_case_names(
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') __ 1
    assert names.count('julian sequeira') __ 0
    assert names.count('Brad Pitt') __ 1
    assert le.(names) __ 10
    assert all(n.title() in names for n in NAMES)


# test_dedup_and_title_case_names()
# pprint(dedup_and_title_case_names(NAMES))
pprint(sort_by_surname_desc(NAMES))
pprint(shortest_first_name(NAMES))
