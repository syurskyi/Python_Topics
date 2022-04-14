c_ Solution:
    ___ shortestCompletingWord  P, words
        """
        :type P: str
        :type words: List[str]
        :rtype: str
        """

        ans ''
        __ n.. P o. n.. words:
            r.. ans

        p_times get_times(P)
        _min_size f__('inf')

        ___ word __ words:
            times get_times(word)
            __ l..(word) < _min_size a.. is_included(p_times, times
                ans word
                _min_size l..(word)

        r.. ans

    ___ is_included  a_times, b_times
        """True if A is a subset of B"""
        ___ char, times __ a_times.i..
            __ char n.. __ b_times:
                r.. F..

            __ b_times[char] < times:
                r.. F..

        r.. T..

    ___ get_times  word
        times    # dict
        ord_a o..('a')
        ord_z o..('z')

        ___ char __ word.l..:
            __ ord_a <_ o..(char) <_ ord_z:
                times[char] times.g.. char, 0) + 1

        r.. times
