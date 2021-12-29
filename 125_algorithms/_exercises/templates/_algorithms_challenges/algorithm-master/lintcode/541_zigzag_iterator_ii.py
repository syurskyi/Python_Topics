"""
Your ZigzagIterator2 object will be instantiated and called as such:
solution, result = ZigzagIterator2(vecs), []
while solution.hasNext(): result.append(solution.next())
Output result
"""


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    ___ __init__(self, vecs):
        self.g = vecs
        self.x = 0
        self.y = 0
        self.max_y = max(l..(vec) ___ vec __ vecs)

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


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    ___ __init__(self, vecs):
        self.queue = [vec ___ vec __ vecs __ vec]

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
