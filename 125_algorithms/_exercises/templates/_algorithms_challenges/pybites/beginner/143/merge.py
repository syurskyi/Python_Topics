NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


___ get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    __ isi..(name, s..):
        age =0
        ___ group __ [group1, group2, group3]:
            __ name.lower() __ group:
                age = group[name.lower()]
        __ age __ 0:
            r.. NOT_FOUND
        ____:
            r.. age
    ____:
        r.. NOT_FOUND

print(get_person_age('thomas'))