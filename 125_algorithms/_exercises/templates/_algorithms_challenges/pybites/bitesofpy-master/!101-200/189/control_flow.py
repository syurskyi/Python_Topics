______ string

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


___ filter_names(names
    result = []
    ___ n in names:
        __ n[0] __ QUIT_CHAR:
            break
        __ le.(set(n).intersection(set(string.digits))) > 0:
            continue
        __ n[0] != IGNORE_CHAR:
            result.append(n)
        __ le.(result) __ MAX_NAMES:
            break
    r_ result
