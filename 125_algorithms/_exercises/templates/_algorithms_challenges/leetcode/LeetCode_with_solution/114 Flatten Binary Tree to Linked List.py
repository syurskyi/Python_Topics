"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..
    ___ __repr__(self):
        r.. repr(self.val)

class Solution:
    ___ flatten_data_structure(self, root):
        """

        :param root: TreeNode
        :return: nothing, do it in place
        """
        # trivial
        __ n.. root:
            r..

        lst    # list
        self.dfs_traverse(root, lst)
        lst = lst[1:] # exclude root

        root.left = N..
        cur = root
        ___ node __ lst:
            node.left = N..
            node.right = N..
            cur.right = node
            cur = cur.right


    ___ dfs_traverse(self, root, lst):
        """
        pre_order traverse
        """
        __ n.. root:
            r..
        lst.a..(root)
        self.dfs_traverse(root.left, lst)
        self.dfs_traverse(root.right, lst)

    ___ flatten(self, root):
        """
        pre-order should be easy
        flatten left subtree
        flatten right subtree
        root->left->right

        in-order is harder to flatten
        http://fisherlei.blogspot.sg/2012/12/leetcode-flatten-binary-tree-to-linked.html
        :param root:
        :return:
        """
        __ n.. root:
            r.. N..


        left_last = self.get_last(root.left)

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        # left_last = left
        # while left_last and left_last.right:
        #     left_last = left_last.right

        root.left = N..
        __ left:
            root.right = left
            left_last.right = right
        ____:
            root.right = right
        r.. root

    ___ get_last(self, root):
        """
        pre-order last
        :param root:
        :return:
        """
        __ n.. root:
            r.. N..
        __ n.. root.left and n.. root.right:
            r.. root
        __ root.right:
            r.. self.get_last(root.right)
        ____:
            r.. self.get_last(root.left)

__ __name____"__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2
    Solution().flatten(node1)

