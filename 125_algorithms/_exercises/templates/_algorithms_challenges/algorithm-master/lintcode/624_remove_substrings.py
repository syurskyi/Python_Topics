c_ Solution:
    """
    @param: s: a string
    @param: D: a set of n substrings
    @return: the minimum length
    """
    ___ minLength  s, D
        __ n.. s:
            r.. 0

        _min l..(s)
        queue [s]
        visited s..([s])

        """
        bfs
                 s
          /----/---\----\
        s-d1 s-d2 s-d3 s-d4
        ...  ...  ...  ...
        """
        ___ s __ queue:
            ___ d __ D:
                found s.find(d)
                w.... found !_ -1:
                    _s s[:found] + s[found + l..(d]
                    found s.find(d, found + 1)

                    __ _s __ visited:
                        _____

                    __ l..(_s) < _min:
                        _min l..(_s)

                    queue.a..(_s)
                    visited.add(_s)

        r.. _min
