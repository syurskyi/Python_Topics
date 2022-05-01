# ____ d.. _______ d..
# ____ d__.p.. _______ p..
# ____ d__.r.. _______ r..
#
# RETURN_FORMAT '{name} was {age} years old when {movie} came out.'
#
#
# ??
# c_ Actor
#     name: s..
#     born: s..
#
#
# ??
# c_ Movie
#     title: s..
#     release_date: s..
#
#
# ___ get_age actor ? movie ? __ s..
#     """Calculates age of actor / actress when movie was released,
#        return a string like this:
#
#        {name} was {age} years old when {movie} came out.
#        e.g.
#        Wesley Snipes was 28 years old when New Jack City came out.
#     """
#     age r.. p.. m__.r.. p.. a__.b__.y..
#     r.. R__.f.. n.._?.n.. m.._?.t.. a.._?
