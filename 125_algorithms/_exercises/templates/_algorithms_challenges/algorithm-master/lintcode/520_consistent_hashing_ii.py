______ bisect
______ random

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    ___ create(cls, n, k
        solution = cls()
        solution.n = n
        solution.k = k
        solution.p2l = {} # point to location
        solution.l2p = {} # location to points
        r_ solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    ___ addMachine(self, machine_id
        item = self.l2p[machine_id] =   # list
        point = -1
        ___ i __ range(self.k
            point = random.randint(0, self.n - 1)
            w___ point __ self.p2l:
                point = random.randint(0, self.n - 1)
            self.p2l[point] = machine_id
            item.append(point)
        item.sort()
        r_ item

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    ___ getMachineIdByHashCode(self, hashcode
        points = sorted(self.p2l.keys())
        index = bisect.bisect_left(points, hashcode) % le.(points)
        # # counterclockwise
        # index = bisect.bisect(points, hashcode) - 1
        # if index < 0:
        #     index = le.(points) - 1
        r_ self.p2l[points[index]]
