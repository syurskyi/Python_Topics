"""
In this bite you will work with a list of names.
First you will write a function to take out duplicates and title case them.
Then you will sort the list in alphabetical descending order by surname and
lastly determine what the shortest first name is.
For this exercise you can assume there is always one name and one surname.
With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""

NAMES =  'arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt' 


___ dedup_and_title_case_names(names
    """Should return a list of names, each name appears only once"""
    new_list    # list
    ___ item __ names:
         __ item.t.. n.. __ new_list:
             new_list.a..(item.t..
    r.. new_list

___ sort_by_surname_desc(names
    """Returns names list sorted desc by surname"""
    r.. s..(names, key=l.... x: x.s..(" ")[1], reverse T..)


___ shortest_first_name(names
    """Returns the shortest first name (str)"""
    r.. s..(names, key=l.... x: l..(x.s..(" ")[0][0].s..(" ")[0]

a dedup_and_title_case_names(NAMES)
print(a)
b sort_by_surname_desc(a)
print(b)
c shortest_first_name(a)
print(c)