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
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    ___ connect(self, root):
        """
        bfs
        same as Populating Next Right Pointers in Each Node I
        :param root: TreeNode
        :return: nothing
        """
        __ not root:
            return None

        q = [root]
        while q:
            current_level = q
            q = []
            for ind, val in enumerate(current_level):
                __ val.left: q.append(val.left)
                __ val.right: q.append(val.right)
                try:
                    val.next = current_level[ind+1]
                except IndexError:
                    val.next = None


