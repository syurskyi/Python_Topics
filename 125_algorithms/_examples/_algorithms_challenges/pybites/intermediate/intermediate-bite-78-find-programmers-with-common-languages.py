"""
Similar as last Bite we do another comparison of sequences exercise.

Here is the deal: you are in charge of huge org of many software devs. You need as many devs for a
new app you want to build so let's do an inventory of the most common languages across the board.
Your input data is a dict of this format:

{'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
 'paul': ['C++', 'JS', 'Python'],
 'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
 'tim': ['Python', 'Haskell', 'C++', 'JS']}
Complete the common_languages function that receives a dict of this format and returns the languages
that ALL devs have in common, so in this case it would return Python and JS. Under TESTS we test
your code against a few more scenarios. Have fun!
"""

programmers = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
 'paul': ['C++', 'JS', 'Python'],
 'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
 'tim': ['Python', 'Haskell', 'C++', 'JS']}

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    sets = []
    for key, value in programmers.items():
        sets.append(set(value))
    first_set = sets[0]
    remaining_sets = sets[1:]
    print(remaining_sets)
    result = first_set.intersection(*remaining_sets)
    print(result)

common_languages(programmers)
