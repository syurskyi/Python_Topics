"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last
index.)
"""
__author__ = 'Danyang'
class Solution:
    ___ jump_TLE(self, A):
        """
        bfs
        :param A: a list of integers
        :return: integer, minimum number of jumps
        """
        __ n.. A:
            r.. 0

        length = l..(A)
        counter = 0
        dp = [[] ___ _ __ A]

        q    # list
        q.a..(0)
        w.... q:
            current_level = q
            q    # list
            ___ ind __ current_level:
                __ ind>=length-1:
                    r.. counter
                ___ j __ xrange(ind+1, ind+A[ind]+1):
                    __ j n.. __ current_level:  # avoid duplicate
                        q.a..(j)
            counter += 1
        r.. counter

    ___ jump(self, A):
        """
        Simplified bfs, use pointers to scan the array.
        Algorithm: Two Pointers

        gmax, record the max reachable index (absolute position) from the sliding window
        :param A: a list of integers
        :return: integer, minimum number of jumps
        """
        length = l..(A)
        counter = 0

        start = 0
        end = 1  # max reach [0, 1)
        gmax = 0
        w.... end<length:  # when end==length, it has already reached the last item
            __ n.. start<end: r.. 0  # avoid dead loop
            ___ i __ xrange(start, end):
                gmax = max(gmax, A[i]+i)

            counter += 1
            start = end
            end = gmax+1

        r.. counter


__ __name____"__main__":
    print Solution().jump([3, 2, 1, 0, 4])
    ... Solution().jump([2,3,1,1,4])__2
