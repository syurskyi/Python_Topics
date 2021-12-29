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
    ___ __init__(self, val, children):
        self.val = val
        self.children = children


____ typing _______ List
____ collections _______ deque


class Solution:
    ___ postorder(self, root: 'Node') -> List[int]:
        """
        maintain a stack, pop and reverse
        """
        __ n.. root:
            r.. []

        ret = deque()
        stk = [root]
        visited = set()
        while stk:
            cur = stk.pop()
            ret.appendleft(cur.val)
            ___ c __ cur.children:
                stk.a..(c)

        r.. l..(ret)
        
    ___ postorder_visited(self, root: 'Node') -> List[int]:
        """
        maintain a stack, if visited before, then pop
        """
        ret    # list
        __ n.. root:
            r.. ret

        stk = [root]
        visited = set()
        while stk:
            cur = stk[-1]
            __ cur __ visited:
                stk.pop()
                ret.a..(cur.val)
            ____:
                visited.add(cur)
                ___ c __ reversed(cur.children):
                    stk.a..(c)

        r.. ret
