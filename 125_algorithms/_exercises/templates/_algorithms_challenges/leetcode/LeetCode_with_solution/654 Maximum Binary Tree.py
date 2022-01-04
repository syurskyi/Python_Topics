#!/usr/bin/python3
"""
Given an integer array with no duplicates. A maximum tree building on this array
is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided
by the maximum number.
The right subtree is the maximum tree constructed from right part subarray
divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this
tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ typing _______ List
_______ heapq


c_ Solution:
    ___ constructMaximumBinaryTree(self, nums: List[i..]) __ TreeNode:
        """
        monotonic stack - a stack to keep a decreasing subsequence from left to
        right
        the cur is the stk[-1]'s right
        the cur's left is elements to its left not in monotonic stack
        """
        stk    # list
        ___ n __ nums:
            cur = TreeNode(n)
            w.... stk a.. stk[-1].val < cur.val:
                left = stk.pop()
                cur.left = left

            __ stk:
                stk[-1].right = cur

            stk.a..(cur)

        r.. stk[0]

c_ Solution_heap:
    ___ constructMaximumBinaryTree(self, nums: List[i..]) __ TreeNode:
        """
        heap O(n lgn)
        insert by index O(n lgn)
        """
        __ n.. nums:
            r..

        h = [(-v, v) ___ v __ nums]
        idx = {
            v: i
            ___ i, v __ e..(nums)
        }
        heapq.heapify(h)
        root = N..
        w.... h:
            _, m = heapq.heappop(h)
            root = insert(root, m, idx)

        r.. root

    ___ insert(self, node, m, idx):
        __ n.. node:
            r.. TreeNode(m)

        __ idx[m] < idx[node.val]:
            node.left = insert(node.left, m, idx)
        ____ idx[m] > idx[node.val]:
            node.right = insert(node.right, m, idx)
        ____:
            raise

        r.. node
