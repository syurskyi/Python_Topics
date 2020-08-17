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
    ___ __init__(self, val, children
        self.val = val
        self.children = children


from typing ______ List


class Solution:
    ___ preorder(self, root: "Node") -> List[int]:
        """
        reversely add the children to stk
        """
        ret = []
        __ not root:
            r_ ret

        stk = [root]
        w___ stk:
            cur = stk.p..
            ret.append(cur.val)
            ___ c in reversed(cur.children
                stk.append(c)

        r_ ret
