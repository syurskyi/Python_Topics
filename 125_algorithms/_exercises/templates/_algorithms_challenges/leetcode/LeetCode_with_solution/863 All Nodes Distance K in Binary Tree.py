#!/usr/bin/python3
"""
We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ distanceK  root: TreeNode, target: TreeNode, K: i..) __ L..[i..]:
        """
        similar to SolutionComplicated
        get its ancestor's distance, but at the same down go down through the tree

        O(N), vist each node 2 times
        """
        ret    # list
        ancestor_dist(root, K, target, ret)
        r.. ret

    ___ dfs_down  node, d, ret
        """
        same as dfs1
        """
        __ n.. node:
            r..
        __ d __ 0:
            ret.a..(node.val)
        ____
            dfs_down(node.left, d - 1, ret)
            dfs_down(node.right, d - 1, ret)

    ___ ancestor_dist  node, K, target, ret
        __ n.. node:
            r.. f__('inf')

        __ node.val __ target.val:
            # d = 0
            dfs_down(node, K, ret)
            r.. 0
        ____
            l = ancestor_dist(node.left, K, target, ret)
            r = ancestor_dist(node.right, K, target, ret)
            d = m..(l, r) + 1
            __ d __ K:
                ret.a..(node.val)
            ____ l __ f__('inf'
                dfs_down(node.left, K - d - 1, ret)
            ____  # r == float('inf')
                dfs_down(node.right, K - d - 1, ret)
            r.. d


c_ SolutionComplicated:
    ___ distanceK  root: TreeNode, target: TreeNode, K: i..) __ L..[i..]:
        """
        break the problem into two part
        1st problem: target's subtree - easy to solve
        2nd problem:  mark parent, ancestor path length
        """
        ret    # list
        dfs1(target, K, ret)
        hm    # dict
        ancestor_dist(root, target, hm)
        dfs2(root, target, K, f__("inf"), hm, ret)
        r.. ret

    ___ dfs1  node, K, ret
        """1st problem"""
        __ n.. node:
            r..

        __ K __ 0:
            ret.a..(node.val)
        ____
            dfs1(node.left, K-1, ret)
            dfs1(node.right, K-1, ret)

    ___ ancestor_dist  node, target, hm
        __ n.. node:
            r.. f__('inf')

        __ node.val __ target.val:
            hm[node.val] = 0
        ____
            left = ancestor_dist(node.left, target, hm)
            right = ancestor_dist(node.right, target, hm)
            hm[node.val] = m..(left, right) + 1

        r.. hm[node.val]

    ___ dfs2  node, target, K, dist, hm, ret
        """2nd problem"""
        __ n.. node:
            r..

        __ node.val __ target.val:
            r..

        dist = m..(dist, hm[node.val])
        __ dist __ K:
            ret.a..(node.val)

        dfs2(node.left, target, K, dist + 1, hm, ret)
        dfs2(node.right, target, K, dist + 1, hm, ret)
