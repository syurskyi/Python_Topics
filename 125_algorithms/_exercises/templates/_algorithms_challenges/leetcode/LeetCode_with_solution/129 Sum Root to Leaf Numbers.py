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
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ sumNumbers(self, root):
        """
        :param root: TreeNode
        :return: Integer
        """
        result    # list
        self.dfs(root, "", result)
        result = [int(element) ___ element __ result]
        r.. s..(result)

    ___ dfs(self, root, cur, result):
        """
        dfs, using string as cur (kind of collector).
        :param root: TreeNode
        :param cur: str
        :param result: list
        :return: None
        """
        __ n.. root:
            r..
        cur = cur+str(root.val)
        __ n.. root.left and n.. root.right:
            result.a..(cur)
            r..

        __ root.left:
            self.dfs(root.left, cur, result)
        __ root.right:
            self.dfs(root.right, cur, result)


    ___ dfs_error(self, root, cur, result):
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

        __ n.. root.left and n.. root.right:
            result.a..(cur)
            r..

        __ root.left:
            self.dfs_error(root.left, cur, result)  # reference to the same list
        __ root.right:
            self.dfs_error(root.right, cur, result)


__ __name____"__main__":
    nodes = [TreeNode(0), TreeNode(1), TreeNode(3)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    Solution().sumNumbers(nodes[0])