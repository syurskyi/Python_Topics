"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..
        next = N..


c_ Solution:
    ___ connect  root):
        """
        bfs
        same as Populating Next Right Pointers in Each Node I
        :param root: TreeNode
        :return: nothing
        """
        __ n.. root:
            r.. N..

        q = [root]
        w.... q:
            current_level = q
            q    # list
            ___ ind, val __ e..(current_level):
                __ val.left: q.a..(val.left)
                __ val.right: q.a..(val.right)
                ___
                    val.next = current_level[ind+1]
                ______ IndexError:
                    val.next = N..


