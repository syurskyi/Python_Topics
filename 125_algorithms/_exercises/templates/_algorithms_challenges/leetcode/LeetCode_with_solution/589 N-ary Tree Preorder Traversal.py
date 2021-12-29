#!/usr/bin/python3
"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    ___ __init__(self, val, children):
        self.val = val
        self.children = children


____ typing _______ List


class Solution:
    ___ preorder(self, root: "Node") -> List[int]:
        """
        reversely add the children to stk
        """
        ret    # list
        __ n.. root:
            r.. ret

        stk = [root]
        w.... stk:
            cur = stk.pop()
            ret.a..(cur.val)
            ___ c __ reversed(cur.children):
                stk.a..(c)

        r.. ret
