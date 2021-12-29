programmers = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    lang_list =  [set(lang_list) for lang_list in programmers.values()]
    return_set = lang_list[0]
    for lang_set in lang_list[1:]:
        return_set = return_set.intersection(lang_set)
    return return_set

print(common_languages(programmers))