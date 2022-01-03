#!/usr/bin/python3
"""
Given the root of a binary tree, each node has a value from 0 to 25 representing
the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents
'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for
example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a
node that has no children.)

Example 1:

Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:

Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:

Input: [2,2,1,null,1,0,null,0]
Output: "abc"

Note:
The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ typing _______ Tuple
____ collections _______ deque


c_ Solution:
    ___ - ):
        mn: Tuple[int] = N..

    ___ smallestFromLeaf(self, root: TreeNode) -> s..:
        """
        dfs
        """
        dfs(root, deque())
        __ n.. mn:
            r.. ""
        r.. "".j..(
            chr(e + ord("a"))
            ___ e __ mn
        )

    ___ dfs(self, node, cur_deque):
        __ n.. node:
            r..

        cur_deque.appendleft(node.val)
        __ n.. node.left a.. n.. node.right:
            t = tuple(cur_deque)
            __ n.. mn o. t < mn:
                mn = t
        ____:
            dfs(node.left, cur_deque)
            dfs(node.right, cur_deque)
        # need to pop at the end
        cur_deque.popleft()
