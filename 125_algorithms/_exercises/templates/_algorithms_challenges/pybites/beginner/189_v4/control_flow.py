_______ string

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


___ filter_names(names):
    result    # list
    ___ n __ names:
        __ n[0] __ QUIT_CHAR:
            break
        __ l..(set(n).intersection(set(string.d..))) > 0:
            continue
        __ n[0] != IGNORE_CHAR:
            result.a..(n)
        __ l..(result) __ MAX_NAMES:
            break
    r.. result
