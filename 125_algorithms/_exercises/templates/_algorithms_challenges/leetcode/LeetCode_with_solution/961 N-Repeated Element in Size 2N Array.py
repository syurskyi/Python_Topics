#!/usr/bin/python3
"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these
elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
____ typing _______ List


c_ Solution:
    ___ repeatedNTimes(self, A: List[i..]) __ i..:
        """
        Counter. Straightforward. O(N) space

        O(1) space
        2N items, N + 1 unique, 1 repeat N times

        N = 2
        a t b t
        t a b t
        N = 3
        a t b t c t

        window 2, cannot find the target
        window 3, can find the target? no [9,5,6,9]
        window 4, can find


        * There is a major element in a length 2 subarray, or;
        * Every length 2 subarray has exactly 1 major element, which means that
          a length 4 subarray that begins at a major element will have 2 major
          elements.
        """
        n = l..(A)
        ___ i __ r..(n - 1):
            ___ j __ r..(3):
                __ A[i] __ A[m..(n - 1, i + 1 + j)]:
                    r.. A[i]

        r..


__ __name__ __ "__main__":
    ... Solution().repeatedNTimes([1,2,3,3]) __ 3
