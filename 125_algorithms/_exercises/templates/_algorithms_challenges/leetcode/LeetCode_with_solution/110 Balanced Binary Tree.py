"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
__author__ = 'Danyang'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ___ __init__(self):
        self.depth_bottom = {}

    ___ isBalanced(self, root):
        self.fathom(root, 0)
        return self._is_balanced(root, 0)

    ___ _is_balanced(self, cur, depth):
        """
        :param depth: depth from root to current node.
        """
        __ not cur:
            return True

        h1 = h2 = depth
        __ cur.left: h1 = self.depth_bottom[cur.left]
        __ cur.right: h2 = self.depth_bottom[cur.right]

        __ abs(h1 - h2) > 1:
            return False

        return all([self._is_balanced(cur.left, depth+1), self._is_balanced(cur.right, depth+1)])

    ___ fathom(self, root, depth):
        __ not root:
            return depth-1

        ret = max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
        self.depth_bottom[root] = ret
        return ret


class SolutionSlow(object):
    ___ isBalanced(self, root):
        """
        pre-order traversal

        :param root: TreeNode
        :return: boolean
        """
        __ not root:
            return True
        __ abs(self.fathom(root.left, 0)-self.fathom(root.right, 0)) > 1:
            return False

        __ self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    ___ fathom(self, root, depth):
        """
        DFS
        """
        __ not root:
            return depth-1  # test cases
        return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
