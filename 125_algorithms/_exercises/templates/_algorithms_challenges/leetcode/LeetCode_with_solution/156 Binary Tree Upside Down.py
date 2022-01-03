"""
Premium Question
"""
__author__ = 'Daniel'


c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(object):
    ___ upsideDownBinaryTree(self, root):
        """
        single recursive

        for each node, upside down the current node's left, and append the current node and its right to the new tree
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root o. n.. root.left:
            r.. root

        left, right = root.left, root.right
        root_new = upsideDownBinaryTree(root.left)
        left.left, left.right = right, root
        root.left, root.right = N.., N..
        r.. root_new


c_ SolutionComplex(object):
    ___ - ):
        root = TreeNode(0)
        cur_new = root

    ___ upsideDownBinaryTree(self, root):
        """
        Tree, iterative + recursive

        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root:
            r..

        traverse(root)
        r.. root

    ___ traverse(self, cur):
        """
        Process left first, and add it to the new tree
        :param cur:
        :return:
        """
        __ n.. cur:
            r..

        __ n.. cur.left:
            cur_new.val = cur.val
            r..

        traverse(cur.left)
        __ cur.right: cur_new.left = TreeNode(cur.right.val)
        cur_new.right = TreeNode(cur.val)
        cur_new = cur_new.right