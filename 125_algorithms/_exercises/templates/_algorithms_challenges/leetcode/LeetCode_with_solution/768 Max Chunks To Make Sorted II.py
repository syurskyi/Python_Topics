#!/usr/bin/python3
"""
This question is the same as "Max Chunks to Make Sorted" except the integers of
the given array are not necessarily distinct, the input array could be up to
length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array
into some number of "chunks" (partitions), and individually sort each chunk.
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
"""
____ t___ _______ L..
____ c.. _______ d.., d..


c_ Solution:
    ___ maxChunksToSorted  arr: L..[i..]) __ i..:
        """
        not necessarily distinct
        sort and assign index
        For the smae element, the right ones should get larget assigned index
        """
        A = s..(arr)
        hm = d..(d..)
        ___ i, e __ e..(A
            hm[e].a..(i)

        proxy    # list
        ___ e __ arr:
            proxy.a..(hm[e].popleft

        ret = 0
        cur_max_idx = 0
        ___ i, e __ e..(proxy
            cur_max_idx = m..(cur_max_idx, e)
            __ cur_max_idx __ i:
                ret += 1

        r.. ret
