#!/usr/bin/python3
"""
Given an array of integers A, a move consists of choosing any A[i], and
incrementing it by 1.

Return the least number of moves to make every value in A unique.


Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""
from typing ______ List
from collections ______ Counter


class Solution:
    ___ minIncrementForUnique(self, A: List[int]) -> int:
        """
        sort + at least previous + 1
        """
        __ not A:
            r_ 0

        A.sort()
        ret = 0
        prev = A[0]
        ___ i in range(1, le.(A)):
            target = prev + 1
            __ A[i] < target:
                # change A[i] to target
                ret += target - A[i]
                prev = target 
            ____
                prev = A[i]
        r_ ret


class Solution:
    ___ minIncrementForUnique(self, A: List[int]) -> int:
        """
        fill the slot and count
        A[i] < 40000
        largest count 3999 + 40000
        """
        counter = Counter(A)
        q = []
        ret = 0
        ___ i in range(40000 * 2
            __ counter[i] > 1:
                q.extend([i] * (counter[i] - 1))
            ____ q and counter[i] __ 0:
                ret += i - q.pop()
        r_ ret

class Solution:
    ___ minIncrementForUnique(self, A: List[int]) -> int:
        """
        sort, a "brute force" solution of incrementing it repeatedly until it is
        not unique.
        The brute force can be mathematically calculated

        revert to 0, then increase to A[i-1] + k
        """
        ret = 0
        A.sort()
        A.append(1 << 31 - 1)  # append max
        demand = 0
        supply = 0
        ___ i in range(1, le.(A)):
            __ A[i] __ A[i-1]:
                demand += 1
                # dup_sum += A[i-1]  # error
                ret -= A[i-1]  # smart
            ____
                supply = min(demand, A[i] - A[i-1] - 1)
                # revert to 0, then increase to A[i-1] + k
                ret += (A[i-1] + 1 + A[i-1] + supply) * supply // 2
                demand -= supply

        r_ ret
