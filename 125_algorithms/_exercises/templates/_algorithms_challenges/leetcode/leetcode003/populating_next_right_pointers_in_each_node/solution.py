"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the
same level, and every parent has two children).

For example,

Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

"""

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c_ Solution(o..
    ___ connect  root
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        __ root __ n.. N..
            __ root.left __ n.. N..
                root.left.next root.right
            __ root.right __ n.. N.. a.. root.next __ n.. N..
                root.right.next root.next.left
            connect(root.left)
            connect(root.right)
