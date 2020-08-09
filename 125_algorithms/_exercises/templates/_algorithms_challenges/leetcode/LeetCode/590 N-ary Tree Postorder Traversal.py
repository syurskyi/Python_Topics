#!/usr/bin/python3
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    ___ __init__(self, val, children
        self.val = val
        self.children = children


from typing ______ List
from collections ______ deque


class Solution:
    ___ postorder(self, root: 'Node') -> List[int]:
        """
        maintain a stack, pop and reverse
        """
        __ not root:
            r_ []

        ret = deque()
        stk = [root]
        visited = set()
        w___ stk:
            cur = stk.pop()
            ret.appendleft(cur.val)
            for c in cur.children:
                stk.append(c)

        r_ list(ret)
        
    ___ postorder_visited(self, root: 'Node') -> List[int]:
        """
        maintain a stack, if visited before, then pop
        """
        ret = []
        __ not root:
            r_ ret

        stk = [root]
        visited = set()
        w___ stk:
            cur = stk[-1]
            __ cur in visited:
                stk.pop()
                ret.append(cur.val)
            ____
                visited.add(cur)
                for c in reversed(cur.children
                    stk.append(c)

        r_ ret
