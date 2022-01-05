"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ zigzagLevelOrder  root):
        """
        BFS, stack & queue
        :param root: a tree node
        :return:  a list of lists of integers
        """
        __ n.. root:
            r.. []

        result    # list
        lst = [root]
        direction = F..
        w.... lst:
            __ direction:
                result.a..([element.val ___ element __ lst])
            ____:
                result.a..([element.val ___ element __ r..(lst)])

            ___ i __ r..(l..(lst)):  # evaluation time
                element = lst.pop(0)  # queue 
                __ element.left:
                    lst.a..(element.left)
                __ element.right:
                    lst.a..(element.right)
            direction = n.. direction
        r.. result


