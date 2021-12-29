NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    non_dup_lst = []
    for x in names:
        if x not in non_dup_lst:
            non_dup_lst.append(x)
    non_dup_lst = [element.title() for element in non_dup_lst]
    return non_dup_lst


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda x: x.split()[1], reverse=False)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_name = [x.split()[0] for x in names]
    shortest_name = min(first_name, key=len)
    return shortest_name