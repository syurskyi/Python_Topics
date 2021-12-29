"""
Your ZigzagIterator object will be instantiated and called as such:
solution, result = ZigzagIterator(v1, v2), []
while solution.hasNext(): result.append(solution.next())
Output result
"""


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ __init__(self, v1, v2):
        self.g = (v1, v2)
        self.x = 0
        self.y = 0
        self.max_y = max(l..(vec) ___ vec __ self.g)

    """
    @return: An integer
    """
    ___ next(self):
        __ n.. self.hasNext():
            r.. -1

        x = self.x
        y = self.y

        self.x += 1

        r.. self.g[x][y]

    """
    @return: True if has next
    """
    ___ hasNext(self):
        while self.y < self.max_y:
            __ (
                self.x < l..(self.g) and
                self.y < l..(self.g[self.x])
            ):
                r.. True

            __ self.x >= l..(self.g):
                self.x = 0
                self.y += 1

            __ self.y >= l..(self.g[self.x]):
                self.x += 1

        r.. False


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ __init__(self, v1, v2):
        self.queue = [vec ___ vec __ (v1, v2) __ vec]

    """
    @return: An integer
    """
    ___ next(self):
        __ n.. self.hasNext():
            r.. -1

        vec = self.queue.pop(0)
        val = vec.pop(0)

        __ vec:
            self.queue.a..(vec)

        r.. val

    """
    @return: True if has next
    """
    ___ hasNext(self):
        r.. bool(self.queue)
