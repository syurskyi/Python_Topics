____ typing _______ List

___ pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    __ N __ 0:
        r.. []
    __ N __ 1:
        r.. [1]
    ____ N > 1:
        line = [1]
        previous_line = pascal(N - 1)
        ___ i __ r..(l..(previous_line) - 1):
            line.a..(previous_line[i] + previous_line[i + 1])
        line += [1]
    r.. line