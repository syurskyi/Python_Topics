#!/usr/bin/python3
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
c_ Node:
    ___ - , val, children
        val = val
        children = children


____ typing _______ List
____ c.. _______ d..


c_ Solution:
    ___ postorder  root: 'Node') __ List[i..]:
        """
        maintain a stack, pop and reverse
        """
        __ n.. root:
            r.. []

        ret = d..()
        stk = [root]
        visited = s..()
        w.... stk:
            cur = stk.pop()
            ret.appendleft(cur.val)
            ___ c __ cur.children:
                stk.a..(c)

        r.. l..(ret)
        
    ___ postorder_visited  root: 'Node') __ List[i..]:
        """
        maintain a stack, if visited before, then pop
        """
        ret    # list
        __ n.. root:
            r.. ret

        stk = [root]
        visited = s..()
        w.... stk:
            cur = stk[-1]
            __ cur __ visited:
                stk.pop()
                ret.a..(cur.val)
            ____:
                visited.add(cur)
                ___ c __ r..(cur.children
                    stk.a..(c)

        r.. ret
