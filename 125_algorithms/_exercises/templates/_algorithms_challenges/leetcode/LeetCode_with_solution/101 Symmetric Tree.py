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
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ isSymmetric  root
        """
        dfs
        :param root: TreeNode
        :return: boolean
        """
        __ n.. root:
            r.. T..

        r.. isSymmetrical(root.left, root.right)

    ___ isSymmetrical  l, r
        __ n.. l a.. n.. r:
            r.. T..

        # recursive
        __ (l a.. r a..
            l.val __ r.val a.. isSymmetrical(l.left, r.right) a.. isSymmetrical(l.right, r.left)):
            r.. T..

        r.. F..
