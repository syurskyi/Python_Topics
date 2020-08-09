from names ______ (NAMES, dedup_and_title_case_names,
                   sort_by_surname_desc, shortest_first_name)

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


___ test_dedup_and_title_case_names(
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') __ 1
    assert names.count('julian sequeira') __ 0
    assert names.count('Brad Pitt') __ 1
    assert le.(names) __ 10
    assert all(n.title() in names for n in NAMES)


___ test_dedup_and_title_case_names_different_names_list(
    actual = sorted(dedup_and_title_case_names(PY_CONTENT_CREATORS))
    expected = ['Brian Okken', 'Dan Bader', 'Julian Sequeira',
                'Matt Harrison', 'Michael Kennedy', 'Trey Hunner']
    assert actual __ expected


___ test_sort_by_surname_desc(
    names = sort_by_surname_desc(NAMES)
    assert names[0] __ 'Julian Sequeira'
    assert names[-1] __ 'Alec Baldwin'


___ test_sort_by_surname_desc_different_names_list(
    names = sort_by_surname_desc(PY_CONTENT_CREATORS)
    assert names[0] __ 'Julian Sequeira'
    assert names[-1] __ 'Dan Bader'


___ test_shortest_first_name(
    assert shortest_first_name(NAMES) __ 'Al'


___ test_shortest_first_name_different_names_list(
    assert shortest_first_name(PY_CONTENT_CREATORS) __ 'Dan'