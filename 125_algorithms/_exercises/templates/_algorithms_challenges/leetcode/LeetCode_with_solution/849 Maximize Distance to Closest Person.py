#!/usr/bin/python3
"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents
that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest
person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has
distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
____ t___ _______ List


c_ Solution:
    ___ maxDistToClosest  seats: List[i..]) __ i..:
        """
        DP from left and right - next array
        Let L[i] be the distant to the left 1 at A[i]
        Let R[i] ...
        """
        n = l..(seats)
        L = [f__("inf") ___ _ __ r..(n)]
        R = [f__("inf") ___ _ __ r..(n)]
        ___ i __ r..(n
            __ seats[i] __ 1:
                L[i] = 0
            ____ i - 1 >= 0:
                L[i] = L[i-1] + 1
        ___ i __ r..(n-1, -1 , -1
            __ seats[i] __ 1:
                R[i] = 0
            ____ i + 1 < n:
                R[i] = R[i+1] + 1

        r.. m..(
            m..(L[i], R[i])
            ___ i __ r..(n)
        )

    ___ maxDistToClosest2  seats: List[i..]) __ i..:
        """
        maintain a sorrted index array
        """
        idxes    # list
        ___ i, e __ e..(seats
            __ e __ 1:
                idxes.a..(i)

        ret = [-f__("inf"), 0]
        n = l..(seats)
        # two ends
        ___ i, j __ z..((0, n-1), (0, -1)):
            dist = abs(i - idxes[j])
            __ dist > ret[0]:
                ret = [dist, i]

        ___ j __ r..(l..(idxes) - 1
            i = (idxes[j] + idxes[j+1]) // 2
            dist = m..(abs(i - idxes[j]), abs(i - idxes[j+1]))
            __ dist > ret[0]:
                ret = [dist, i]

        r.. ret[0]


__ _______ __ _______
    ... Solution().maxDistToClosest([1,0,0,0,1,0,1]) __ 2
