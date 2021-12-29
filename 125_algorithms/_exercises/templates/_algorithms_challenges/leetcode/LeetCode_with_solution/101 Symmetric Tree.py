"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'


# Definition for a  binary tree node
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ isSymmetric(self, root):
        """
        dfs
        :param root: TreeNode
        :return: boolean
        """
        __ n.. root:
            r.. True

        r.. self.isSymmetrical(root.left, root.right)

    ___ isSymmetrical(self, l, r):
        __ n.. l a.. n.. r:
            r.. True

        # recursive
        __ (l a.. r a..
            l.val __ r.val a.. self.isSymmetrical(l.left, r.right) a.. self.isSymmetrical(l.right, r.left)):
            r.. True

        r.. False
