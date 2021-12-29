def get_index_different_char(chars):
    alphanumeric, non_alphanumeric = set(), set()
    for i, c in enumerate(chars):
        if str.isalnum(str(c)):
            alphanumeric.add(i)
        else:
            non_alphanumeric.add(i)
    return next(iter(alphanumeric)) \
        if len(alphanumeric) == 1 \
        else next(iter(non_alphanumeric))