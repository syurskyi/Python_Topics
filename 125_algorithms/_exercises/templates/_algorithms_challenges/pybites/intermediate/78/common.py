programmers = d..(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])

___ common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    lang_list =  [set(lang_list) ___ lang_list __ programmers.v..
    return_set = lang_list[0]
    ___ lang_set __ lang_list[1:]:
        return_set = return_set.intersection(lang_set)
    r.. return_set

print(common_languages(programmers))