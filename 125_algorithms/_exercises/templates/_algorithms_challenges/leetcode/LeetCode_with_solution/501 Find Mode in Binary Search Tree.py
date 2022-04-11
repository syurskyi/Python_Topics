#!/usr/bin/python3
"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most
frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to
the node's key.
The right subtree of a node contains only nodes with keys greater than or equal
to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the
implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ findMode  root
        """
        In-order traversal
        O(1) space thus cannot keep a set of current modes
        need two passes - 1st pass to find the mode count, 2nd pass to find all
        modes equal to the mode count

        :type root: TreeNode
        :rtype: List[int]
        """
        ret [[], 0]  # [results, length]
        find_mode(root, [N.., 0], ret, F..)
        find_mode(root, [N.., 0], ret, T..)
        r.. ret[0]

    ___ find_mode  root, prev, ret, collect
        """
        prev: [previous_value, count]. Need to survice the call stack
        """
        __ n.. root:
            r..

        find_mode(root.left, prev, ret, collect)

        __ prev[0] __ root.val:
            prev[1] += 1
        ____
            prev[1] 1
        prev[0] root.val

        __ n.. collect:
            ret[1] m..(ret[1], prev[1])
        ____
            __ prev[1] __ ret[1]:
                ret[0].a..(root.val)

        find_mode(root.right, prev, ret, collect)

    ___ findMode_error  root
        """
        counter (extra space) for any tree
        use recursion

        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root:
            r.. []

        ret [0, []]
        find_mode_error(root, root.val, ret)
        r.. ret[1]

    ___ find_mode_error  root, target, ret
        cur 0
        __ n.. root:
            r.. cur

        __ root.val __ target:
            cur += 1
            cur += find_mode_error(root.left, root.val, ret)
            cur += find_mode_error(root.right, root.val, ret)
            __ cur > ret[0]:
                ret[0], ret[1] cur, [target]
            ____ cur __ ret[0]:
                ret[1].a..(target)
        ____
            find_mode_error(root, root.val, ret)

        r.. cur
