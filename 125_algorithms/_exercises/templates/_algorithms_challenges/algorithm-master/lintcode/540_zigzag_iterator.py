"""
Your ZigzagIterator object will be instantiated and called as such:
solution, result = ZigzagIterator(v1, v2), []
while solution.hasNext(): result.append(solution.next())
Output result
"""


c_ ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ - , v1, v2):
        g = (v1, v2)
        x = 0
        y = 0
        max_y = m..(l..(vec) ___ vec __ g)

    """
    @return: An integer
    """
    ___ next
        __ n.. hasNext
            r.. -1

        x = x
        y = y

        x += 1

        r.. g[x][y]

    """
    @return: True if has next
    """
    ___ hasNext
        w.... y < max_y:
            __ (
                x < l..(g) a..
                y < l..(g[x])
            ):
                r.. T..

            __ x >= l..(g):
                x = 0
                y += 1

            __ y >= l..(g[x]):
                x += 1

        r.. F..


c_ ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ - , v1, v2):
        queue = [vec ___ vec __ (v1, v2) __ vec]

    """
    @return: An integer
    """
    ___ next
        __ n.. hasNext
            r.. -1

        vec = queue.pop(0)
        val = vec.pop(0)

        __ vec:
            queue.a..(vec)

        r.. val

    """
    @return: True if has next
    """
    ___ hasNext
        r.. b..(queue)
