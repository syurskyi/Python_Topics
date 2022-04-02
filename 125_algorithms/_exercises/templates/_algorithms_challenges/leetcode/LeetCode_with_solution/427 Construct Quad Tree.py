#!/usr/bin/python3
"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid
can only be true or false. The root node represents the whole grid. For each
node, it will be subdivided into four children nodes until the values in the
region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if
and only if the node is a leaf node. The val attribute for a leaf node contains
the value of the region it represents.
"""
__author__ = 'Danyang'


# Definition for a QuadTree node.
c_ Node:
    ___ - , val, isLeaf, topLeft, topRight, bottomLeft, bottomRight
        val = val
        isLeaf = isLeaf
        topLeft = topLeft
        topRight = topRight
        bottomLeft = bottomLeft
        bottomRight = bottomRight


c_ Solution:
    ___ construct  grid
        """
        DPS, check 4 children then merge

        :type grid: List[List[int]]
        :rtype: Node
        """
        l = l..(grid)
        r.. _construct(grid, 0, 0, l)

    ___ _construct  grid, row, col, l
        """
        Use row col for matrix rather than x y coordiate since the direction is
        error-prone
        """
        __ l __ 1:
            r.. Node(grid[row][col], T.., N.., N.., N.., N..)

        l_child = l // 2
        topLeft = _construct(grid, row, col, l_child)
        topRight = _construct(grid, row, col + l_child, l_child)
        bottomLeft = _construct(grid, row + l_child, col, l_child)
        bottomRight = _construct(grid, row + l_child, col + l_child, l_child)
        is_leaf = (
            topLeft.val __ topRight.val __ bottomLeft.val __ bottomRight.val
            != "*"
        )
        __ is_leaf:
            r.. Node(grid[row][col], T.., N.., N.., N.., N..)

        r.. Node("*", F.., topLeft, topRight, bottomLeft, bottomRight)
