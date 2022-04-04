"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
__author__ = 'Danyang'


c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ -
        depth_bottom    # dict

    ___ isBalanced  root
        fathom(root, 0)
        r.. _is_balanced(root, 0)

    ___ _is_balanced  cur, depth
        """
        :param depth: depth from root to current node.
        """
        __ n.. cur:
            r.. T..

        h1 = h2 = depth
        __ cur.left: h1 = depth_bottom[cur.left]
        __ cur.right: h2 = depth_bottom[cur.right]

        __ a..(h1 - h2) > 1:
            r.. F..

        r.. a..([_is_balanced(cur.left, depth+1), _is_balanced(cur.right, depth+1)])

    ___ fathom  root, depth
        __ n.. root:
            r.. depth-1

        ret = m..(fathom(root.left, depth+1), fathom(root.right, depth+1
        depth_bottom[root] = ret
        r.. ret


c_ SolutionSlow(o..
    ___ isBalanced  root
        """
        pre-order traversal

        :param root: TreeNode
        :return: boolean
        """
        __ n.. root:
            r.. T..
        __ a..(fathom(root.left, 0)-fathom(root.right, 0 > 1:
            r.. F..

        __ isBalanced(root.left) a.. isBalanced(root.right
            r.. T..
        ____
            r.. F..

    ___ fathom  root, depth
        """
        DFS
        """
        __ n.. root:
            r.. depth-1  # test cases
        r.. m..(fathom(root.left, depth+1), fathom(root.right, depth+1
