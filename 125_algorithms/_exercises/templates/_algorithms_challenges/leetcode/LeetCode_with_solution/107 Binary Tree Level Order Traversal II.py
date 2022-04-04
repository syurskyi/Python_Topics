"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ levelOrderBottom  root
        """
        bfs
        :param root: TreeNode
        :return: Integers
        """
        __ n.. root:
            r.. []
        result    # list
        next_level = [root]
        w.... next_level:
            current_level = next_level
            result.insert(0, map(l.... x: x.val, current_level  # current level, only difference with Binary Tree Level Order Traversal I

            next_level    # list
            ___ element __ current_level:
                __ element.left:
                    next_level.a..(element.left)
                __ element.right:
                    next_level.a..(element.right)
        r.. result

__ _____ __ ____
    Solution().levelOrderBottom(TreeNode(1










