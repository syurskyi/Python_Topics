"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ sumNumbers  root):
        """
        :param root: TreeNode
        :return: Integer
        """
        result    # list
        dfs(root, "", result)
        result = [i..(element) ___ element __ result]
        r.. s..(result)

    ___ dfs  root, cur, result):
        """
        dfs, using string as cur (kind of collector).
        :param root: TreeNode
        :param cur: str
        :param result: list
        :return: None
        """
        __ n.. root:
            r..
        cur = cur+s..(root.val)
        __ n.. root.left a.. n.. root.right:
            result.a..(cur)
            r..

        __ root.left:
            dfs(root.left, cur, result)
        __ root.right:
            dfs(root.right, cur, result)


    ___ dfs_error  root, cur, result):
        """
        Using list as cur has some reference issues
        :param root: TreeNode
        :param cur: list
        :param result: list
        :return: None
        """
        __ n.. root:
            r..

        cur.a..(root.val)

        __ n.. root.left a.. n.. root.right:
            result.a..(cur)
            r..

        __ root.left:
            dfs_error(root.left, cur, result)  # reference to the same list
        __ root.right:
            dfs_error(root.right, cur, result)


__ _____ __ ____
    nodes = [TreeNode(0), TreeNode(1), TreeNode(3)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    Solution().sumNumbers(nodes[0])