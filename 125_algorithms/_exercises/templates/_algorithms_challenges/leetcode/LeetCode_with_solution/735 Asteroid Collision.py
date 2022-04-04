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
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each
other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
____ t___ _______ L..


c_ Solution:
    ___ asteroidCollision  asteroids: L..[i..]) __ L..[i..]:
        """
        simplified

        while-else: break statement break the entire while-else block
        for-else: break statement break the entire for-else block

        stack from left to right, only -> <- will pop the stack
        """
        stk    # list
        ___ e __ asteroids:
            w.... stk a.. e < 0 < stk[-1]:
                __ a..(e) > a..(stk[-1]
                    # -> exploded, <- continues
                    stk.p.. )
                ____ a..(e) __ a..(stk[-1]
                    # -> <- both exploded
                    stk.p.. )
                    _____
                ____
                    # <- exploded, -> continue
                    _____
            ____
                stk.a..(e)

        r.. stk

    ___ asteroidCollision_complex  asteroids: L..[i..]) __ L..[i..]:
        """
        asteroids same speed
        list of size

        stk of index

        only -> <- will collide
        """
        stk    # list
        n = l..(asteroids)
        ___ i __ r..(n-1, -1, -1
            cur = asteroids[i]
            w.... stk a.. asteroids[stk[-1]] < 0 a.. cur > 0 a.. a..(asteroids[stk[-1]]) < a..(cur
                stk.p.. )

            __ stk a.. cur > 0 a.. asteroids[stk[-1]] __ -cur:
                stk.p.. )
                _____

            __ n.. stk:
                stk.a..(i)
                _____

            __ n.. (asteroids[stk[-1]] < 0 a.. cur > 0) o. a..(cur) > a..(asteroids[stk[-1]]
                stk.a..(i)

        r.. [
            asteroids[i]
            ___ i __ stk[::-1]
        ]


__ _______ __ _______
    ... Solution().asteroidCollision([10, 2, -5]) __ [10]
    ... Solution().asteroidCollision([5, 10, -5]) __ [5, 10]
    ... Solution().asteroidCollision([8, -8]) __ []
