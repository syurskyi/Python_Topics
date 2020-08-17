#!/usr/bin/python3
"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. Two
asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, w___ the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each
other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
from typing ______ List


class Solution:
    ___ asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        simplified

        w___-else: break statement break the entire w___-else block
        for-else: break statement break the entire for-else block

        stack from left to right, only -> <- will pop the stack
        """
        stk = []
        ___ e in asteroids:
            w___ stk and e < 0 < stk[-1]:
                __ abs(e) > abs(stk[-1]
                    # -> exploded, <- continues
                    stk.p..
                ____ abs(e) __ abs(stk[-1]
                    # -> <- both exploded
                    stk.p..
                    break
                ____
                    # <- exploded, -> continue
                    break
            ____
                stk.append(e)

        r_ stk

    ___ asteroidCollision_complex(self, asteroids: List[int]) -> List[int]:
        """
        asteroids same speed
        list of size

        stk of index

        only -> <- will collide
        """
        stk = []
        n = le.(asteroids)
        ___ i in range(n-1, -1, -1
            cur = asteroids[i]
            w___ stk and asteroids[stk[-1]] < 0 and cur > 0 and abs(asteroids[stk[-1]]) < abs(cur
                stk.p..

            __ stk and cur > 0 and asteroids[stk[-1]] __ -cur:
                stk.p..
                continue

            __ not stk:
                stk.append(i)
                continue

            __ not (asteroids[stk[-1]] < 0 and cur > 0) or abs(cur) > abs(asteroids[stk[-1]]
                stk.append(i)

        r_ [
            asteroids[i]
            ___ i in stk[::-1]
        ]


__ __name__ __ "__main__":
    assert Solution().asteroidCollision([10, 2, -5]) __ [10]
    assert Solution().asteroidCollision([5, 10, -5]) __ [5, 10]
    assert Solution().asteroidCollision([8, -8]) __ []
