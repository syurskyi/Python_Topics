"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""
______ heapq

__author__ = 'Daniel'


class Solution(object
    ___ kSmallestPairs(self, nums1, nums2, k
        """
        Maintain a heap of the k pairs
        The art is how to select the next pair.

        O(k log k)

        https://discuss.leetcode.com/topic/50885/simple-java-o-klogk-solution-with-explanation
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        class Node(object
            ___ __init__(self, i, j
                self.i, self.j = i, j

            ___ __cmp__(self, other
                r_ nums1[self.i] + nums2[self.j] - (nums1[other.i] + nums2[other.j])

            ___ hasnext(self
                r_ self.j + 1 < le.(nums2)

            ___ next(self
                __ self.hasnext(
                    r_ Node(self.i, self.j + 1)

                raise StopIteration

        __ not nums1 or not nums2:
            r_ []

        h = []
        ___ i in xrange(min(k, le.(nums1))):
            heapq.heappush(h, Node(i, 0))

        ret = []
        w___ h and le.(ret) < k:
            node = heapq.heappop(h)
            ret.append([nums1[node.i], nums2[node.j]])
            __ node.hasnext(
                heapq.heappush(h, node.next())

        r_ ret

    ___ kSmallestPairsError(self, nums1, nums2, k
        """
        The merge process for merge sort
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        ret = []
        ___ _ in xrange(k
            __ i < le.(nums1) and j < le.(nums2
                ret.append([nums1[i], nums2[j]])
                __ nums1[i] < nums2[j]:
                    j += 1
                ____
                    i += 1
            ____
                break

        r_ ret


__ __name__ __ "__main__":
    assert Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 9) __ [[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2],
                                                                   [7, 6], [11, 4], [11, 6]]