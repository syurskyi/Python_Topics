"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
__author__ 'Daniel'


c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ binaryTreePaths  root
        """

        :type root: TreeNode
        :rtype: list[str]
        """
        __ n.. root:
            r.. []

        ret    # list
        dfs(root, [], ret)
        r.. ret

    ___ dfs  cur, p.., ret
        """
        pre-check
        """
        p...a..(cur)
        __ n.. cur.left a.. n.. cur.right:
            ret.a..("->".j.. m..(l.... x: s..(x.val), p..)))
            r..

        __ cur.left:
            dfs(cur.left, p.., ret)
            p...p.. )  # pop the shared path

        __ cur.right:
            dfs(cur.right, p.., ret)
            p...p.. )  # pop the shared path

    ___ dfs_path  cur, p.., ret
        __ n.. cur:
            r..

        p...a..(cur)
        __ n.. cur.left a.. n.. cur.right:
            ret.a..("->".j.. m..(l.... x: s..(x.val), p..)))

        dfs_path(cur.left, p.., ret)
        dfs_path(cur.right, p.., ret)
        p...p.. )
