___ get_index_different_char(chars):
    alphanumeric, non_alphanumeric = set(), set()
    ___ i, c __ enumerate(chars):
        __ str.isalnum(str(c)):
            alphanumeric.add(i)
        ____:
            non_alphanumeric.add(i)
    r.. next(iter(alphanumeric)) \
        __ l..(alphanumeric) __ 1 \
        ____ next(iter(non_alphanumeric))