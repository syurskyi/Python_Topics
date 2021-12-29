_______ bisect
_______ random

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    ___ create(cls, n, k):
        solution = cls()
        solution.n = n
        solution.k = k
        solution.p2l = {} # point to location
        solution.l2p = {} # location to points
        r.. solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    ___ addMachine(self, machine_id):
        item = self.l2p[machine_id]    # list
        point = -1
        ___ i __ r..(self.k):
            point = random.randint(0, self.n - 1)
            w.... point __ self.p2l:
                point = random.randint(0, self.n - 1)
            self.p2l[point] = machine_id
            item.a..(point)
        item.s..()
        r.. item

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    ___ getMachineIdByHashCode(self, hashcode):
        points = s..(self.p2l.keys())
        index = bisect.bisect_left(points, hashcode) % l..(points)
        # # counterclockwise
        # index = bisect.bisect(points, hashcode) - 1
        # if index < 0:
        #     index = len(points) - 1
        r.. self.p2l[points[index]]
