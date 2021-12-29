import functools
___ common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""


    sets = map(set,programmers.values())



    return functools.reduce(lambda x,y: x.intersection(y),sets)





