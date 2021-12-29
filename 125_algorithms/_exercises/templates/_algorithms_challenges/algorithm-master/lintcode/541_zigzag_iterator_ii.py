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
        self.max_y = max(len(vec) for vec in vecs)

    """
    @return: An integer
    """
    ___ next(self):
        __ not self.hasNext():
            return -1

        x = self.x
        y = self.y

        self.x += 1

        return self.g[x][y]

    """
    @return: True if has next
    """
    ___ hasNext(self):
        while self.y < self.max_y:
            __ (
                self.x < len(self.g) and
                self.y < len(self.g[self.x])
            ):
                return True

            __ self.x >= len(self.g):
                self.x = 0
                self.y += 1

            __ self.y >= len(self.g[self.x]):
                self.x += 1

        return False


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    ___ __init__(self, vecs):
        self.queue = [vec for vec in vecs __ vec]

    """
    @return: An integer
    """
    ___ next(self):
        __ not self.hasNext():
            return -1

        vec = self.queue.pop(0)
        val = vec.pop(0)

        __ vec:
            self.queue.append(vec)

        return val

    """
    @return: True if has next
    """
    ___ hasNext(self):
        return bool(self.queue)
