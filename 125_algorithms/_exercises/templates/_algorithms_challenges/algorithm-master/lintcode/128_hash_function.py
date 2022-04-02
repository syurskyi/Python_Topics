c_ Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    ___ hashCode  key, HASH_SIZE
        __ n.. key:
            r.. 0

        MAGIC_NUMBER = 33

        _code = 0
        ___ char __ key:
            _code = (_code * MAGIC_NUMBER + o..(char)) % HASH_SIZE

        r.. _code
