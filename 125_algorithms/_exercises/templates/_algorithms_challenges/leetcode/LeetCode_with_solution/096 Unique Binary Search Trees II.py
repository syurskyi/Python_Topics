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
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ -
        cache    # dict

    ___ generateTrees  n
        """
        dfs
        Catalan
        :param n: integer
        :return: list of TreeNode
        """
        __ n __ 0:
            r.. [N..]

        r.. generate_cache(1, n)

    ___ generate_cache  start, end
        """80ms"""
        __ (start, end) n.. __ cache:
            roots    # list
            __ start > end:
                roots.a..(N..)
                r.. roots

            ___ pivot __ r..(start, end+1
                left_roots = generate_cache(start, pivot-1)
                right_roots = generate_cache(pivot+1, end)
                ___ left_root __ left_roots:
                    ___ right_root __ right_roots:
                        root = TreeNode(pivot)
                        root.left = left_root
                        root.right = right_root

                        roots.a..(root)

            cache[(start, end)] = roots

        r.. cache[(start, end)]

    ___ generate  start, end
        """
        dfs (cache possible)
        100 ms
        {number| number \in [start, end]}

        Follow the 1st proof of Catalan Number
        :param start: initial number in the array
        :param end: final number in the array
        :return: list of TreeNode
        """
        subtree_roots    # list

        # trivial
        __ start > end:
            subtree_roots.a..(N..)
            r.. subtree_roots

        # pivot
        # list of unique subtrees = list of unique left subtrees, pivot, list of unique right subtrees
        ___ pivot __ r..(start, end+1
            left_subtree_roots = generate(start, pivot-1)
            right_subtree_roots = generate(pivot+1, end)

            ___ left_node __ left_subtree_roots:
                ___ right_node __ right_subtree_roots:
                    pivot_node = TreeNode(pivot)
                    pivot_node.left = left_node
                    pivot_node.right = right_node

                    subtree_roots.a..(pivot_node)

        r.. subtree_roots
