#! /usr/bin/env python
# -*- coding: utf-8 -*-


___ generateParenthesis  n
    """
    :type n: int
    :rtype: List[str]
    """

    # node = [leftchild, rightchild, count"(", count")", current str]
    __ n.. n:
        r_ [""]
    solution   # list
    root = [None, None, 1, 0, "("]
    self.generate_child_tree(root, n, solution)
    r_ solution


___ generate_child_tree  node, n, solution
    # the node is the leave and the str is what we want
    __ node[2] __ node[3] __ n:
        node[0] = None
        node[1] = None
        solution.a.. node[4])

    # the node have both left and right child
    ____ node[2] > node[3] a.. node[2] < n:
        left_child = [None, None, node[2] + 1, node[3], node[4] + "("]
        right_child = [None, None, node[2], node[3] + 1, node[4] + ")"]
        node[0] = left_child
        node[1] = right_child
        self.generate_child_tree(left_child, n, solution)
        self.generate_child_tree(right_child, n, solution)

    # the node have only left child
    ____ node[2] __ node[3] a.. node[2] < n:
        left_child = [None, None, node[2] + 1, node[3], node[4] + "("]
        node[0] = left_child
        self.generate_child_tree(left_child, n, solution)

    # the node have only left child
    ____
        right_child = [None, None, node[2], node[3] + 1, node[4] + ")"]
        node[1] = right_child
        self.generate_child_tree(right_child, n, solution)

"""
0
1
3
5
"""
