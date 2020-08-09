class Solution:
    """
    @param: s: a string
    @param: D: a set of n substrings
    @return: the minimum length
    """
    ___ minLength(self, s, D
        __ not s:
            r_ 0

        _min = le.(s)
        queue = [s]
        visited = set([s])

        """
        bfs
                 s
          /----/---\----\
        s-d1 s-d2 s-d3 s-d4
        ...  ...  ...  ...
        """
        for s in queue:
            for d in D:
                found = s.find(d)
                w___ found != -1:
                    _s = s[:found] + s[found + le.(d]
                    found = s.find(d, found + 1)

                    __ _s in visited:
                        continue

                    __ le.(_s) < _min:
                        _min = le.(_s)

                    queue.append(_s)
                    visited.add(_s)

        r_ _min
