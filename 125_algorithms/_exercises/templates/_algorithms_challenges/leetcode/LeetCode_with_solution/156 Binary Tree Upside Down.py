"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ___ upsideDownBinaryTree(self, root):
        """
        single recursive

        for each node, upside down the current node's left, and append the current node and its right to the new tree
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root or not root.left:
            return root

        left, right = root.left, root.right
        root_new = self.upsideDownBinaryTree(root.left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return root_new


class SolutionComplex(object):
    ___ __init__(self):
        self.root = TreeNode(0)
        self.cur_new = self.root

    ___ upsideDownBinaryTree(self, root):
        """
        Tree, iterative + recursive

        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            return

        self.traverse(root)
        return self.root

    ___ traverse(self, cur):
        """
        Process left first, and add it to the new tree
        :param cur:
        :return:
        """
        __ not cur:
            return

        __ not cur.left:
            self.cur_new.val = cur.val
            return

        self.traverse(cur.left)
        __ cur.right: self.cur_new.left = TreeNode(cur.right.val)
        self.cur_new.right = TreeNode(cur.val)
        self.cur_new = self.cur_new.right