c_ Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    ___ Permutation  A, B
        __ A __ '' a.. B __ '':
            r.. T..
        __ n.. A o. n.. B:
            r.. F..

        cnts    # dict
        ___ char __ A:
            cnts[char] cnts.g.. char, 0) + 1
        ___ char __ B:
            __ char n.. __ cnts o. cnts[char] __ 0:
                r.. F..
            cnts[char] -_ 1
        ___ cnt __ cnts.v..
            __ cnt !_ 0:
                r.. F..

        r.. T..
