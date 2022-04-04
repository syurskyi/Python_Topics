"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    """
    find path count
    """
    ___ pathSum  root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. s..((
            count_valid_path(root, target),
            pathSum(root.left, target),
            pathSum(root.right, target),


    ___ count_valid_path  node, remaining
        __ n.. node:
            r.. 0

        r.. s..((
            i..(node.val __ remaining),
            count_valid_path(node.left, remaining - node.val),
            count_valid_path(node.right, remaining - node.val),



c_ Solution:
    """
    print path
    """
    ___ pathSum  root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. root:
            r.. ans

        dfs(root, target, ans, [])

        r.. ans

    ___ dfs  node, target, ans, p..
        __ n.. node:
            r..

        p...a..(node.val)

        remaining = target
        ___ i __ r..(l..(p..) - 1, -1, -1
            remaining -= p..[i]

            __ remaining __ 0:
                ans.a..(p..[i:])

        dfs(node.left, target, ans, p..)
        dfs(node.right, target, ans, p..)
        p...pop()
