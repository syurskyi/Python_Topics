import string

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


___ filter_names(names):
    result = []
    for n in names:
        __ n[0] == QUIT_CHAR:
            break
        __ len(set(n).intersection(set(string.digits))) > 0:
            continue
        __ n[0] != IGNORE_CHAR:
            result.append(n)
        __ len(result) == MAX_NAMES:
            break
    return result
