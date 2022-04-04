_______ bisect
_______ r__

c_ Solution:
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
        solution.p2l    # dict # point to location
        solution.l2p    # dict # location to points
        r.. solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    ___ addMachine  machine_id
        item = l2p[machine_id]    # list
        point = -1
        ___ i __ r..(k
            point = r__.r..(0, n - 1)
            w.... point __ p2l:
                point = r__.r..(0, n - 1)
            p2l[point] = machine_id
            item.a..(point)
        item.s..()
        r.. item

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    ___ getMachineIdByHashCode  hashcode
        points = s..(p2l.keys
        index = bisect.bisect_left(points, hashcode) % l..(points)
        # # counterclockwise
        # index = bisect.bisect(points, hashcode) - 1
        # if index < 0:
        #     index = len(points) - 1
        r.. p2l[points[index]]
