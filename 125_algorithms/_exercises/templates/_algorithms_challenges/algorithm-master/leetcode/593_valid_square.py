class Solution:
    ___ validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ps    # list

        ___ p __ (p1, p2, p3, p4):
            __ n.. p:
                r.. False

            ps.a..(p)

        ps.s..()

        # 0: lb, 1: lt, 2:rb, 3: rt
        l01 = self.get_distance(ps[0], ps[1])
        l02 = self.get_distance(ps[0], ps[2])
        l13 = self.get_distance(ps[1], ps[3])
        l23 = self.get_distance(ps[2], ps[3])

        l03 = self.get_distance(ps[0], ps[3])
        l12 = self.get_distance(ps[1], ps[2])

        r.. a..((
            l01 __ l02 __ l13 __ l23 > 0,
            l03 __ l12,
        ))

    ___ get_distance(self, a, b):
        """
        find the size of 'ab'
        """
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        r.. (dx * dx + dy * dy) ** 0.5
