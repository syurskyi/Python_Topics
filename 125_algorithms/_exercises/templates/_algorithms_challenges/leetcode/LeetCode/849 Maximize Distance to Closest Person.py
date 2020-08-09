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
from typing ______ List


class Solution:
    ___ maxDistToClosest(self, seats: List[int]) -> int:
        """
        DP from left and right - next array
        Let L[i] be the distant to the left 1 at A[i]
        Let R[i] ...
        """
        n = le.(seats)
        L = [float("inf") ___ _ in range(n)]
        R = [float("inf") ___ _ in range(n)]
        ___ i in range(n
            __ seats[i] __ 1:
                L[i] = 0
            ____ i - 1 >= 0:
                L[i] = L[i-1] + 1
        ___ i in range(n-1, -1 , -1
            __ seats[i] __ 1:
                R[i] = 0
            ____ i + 1 < n:
                R[i] = R[i+1] + 1

        r_ max(
            min(L[i], R[i])
            ___ i in range(n)
        )

    ___ maxDistToClosest2(self, seats: List[int]) -> int:
        """
        maintain a sorrted index array
        """
        idxes = []
        ___ i, e in enumerate(seats
            __ e __ 1:
                idxes.append(i)

        ret = [-float("inf"), 0]
        n = le.(seats)
        # two ends
        ___ i, j in zip((0, n-1), (0, -1)):
            dist = abs(i - idxes[j])
            __ dist > ret[0]:
                ret = [dist, i]

        ___ j in range(le.(idxes) - 1
            i = (idxes[j] + idxes[j+1]) // 2
            dist = min(abs(i - idxes[j]), abs(i - idxes[j+1]))
            __ dist > ret[0]:
                ret = [dist, i]

        r_ ret[0]


__ __name__ __ "__main__":
    assert Solution().maxDistToClosest([1,0,0,0,1,0,1]) __ 2
