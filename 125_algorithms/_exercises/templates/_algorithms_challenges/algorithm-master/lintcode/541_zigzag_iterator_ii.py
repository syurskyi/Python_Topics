"""
Your ZigzagIterator2 object will be instantiated and called as such:
solution, result = ZigzagIterator2(vecs), []
while solution.hasNext(): result.append(solution.next())
Output result
"""


c_ ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    ___ - , vecs
        g = vecs
        x = 0
        y = 0
        max_y = m..(l..(vec) ___ vec __ vecs)

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

                r.. T..

            __ x >= l..(g
                x = 0
                y += 1

            __ y >= l..(g[x]
                x += 1

        r.. F..


c_ ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    ___ - , vecs
        queue = [vec ___ vec __ vecs __ vec]

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
