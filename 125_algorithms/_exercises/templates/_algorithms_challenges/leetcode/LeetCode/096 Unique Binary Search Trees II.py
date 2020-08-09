"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'


# Definition for a  binary tree node
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution(object
    ___ __init__(self
        self.cache = {}

    ___ generateTrees(self, n
        """
        dfs
        Catalan
        :param n: integer
        :return: list of TreeNode
        """
        __ n __ 0:
            r_ [None]

        r_ self.generate_cache(1, n)

    ___ generate_cache(self, start, end
        """80ms"""
        __ (start, end) not in self.cache:
            roots = []
            __ start > end:
                roots.append(None)
                r_ roots

            ___ pivot in range(start, end+1
                left_roots = self.generate_cache(start, pivot-1)
                right_roots = self.generate_cache(pivot+1, end)
                ___ left_root in left_roots:
                    ___ right_root in right_roots:
                        root = TreeNode(pivot)
                        root.left = left_root
                        root.right = right_root

                        roots.append(root)

            self.cache[(start, end)] = roots

        r_ self.cache[(start, end)]

    ___ generate(self, start, end
        """
        dfs (cache possible)
        100 ms
        {number| number \in [start, end]}

        Follow the 1st proof of Catalan Number
        :param start: initial number in the array
        :param end: final number in the array
        :return: list of TreeNode
        """
        subtree_roots = []

        # trivial
        __ start > end:
            subtree_roots.append(None)
            r_ subtree_roots

        # pivot
        # list of unique subtrees = list of unique left subtrees, pivot, list of unique right subtrees
        ___ pivot in range(start, end+1
            left_subtree_roots = self.generate(start, pivot-1)
            right_subtree_roots = self.generate(pivot+1, end)

            ___ left_node in left_subtree_roots:
                ___ right_node in right_subtree_roots:
                    pivot_node = TreeNode(pivot)
                    pivot_node.left = left_node
                    pivot_node.right = right_node

                    subtree_roots.append(pivot_node)

        r_ subtree_roots
