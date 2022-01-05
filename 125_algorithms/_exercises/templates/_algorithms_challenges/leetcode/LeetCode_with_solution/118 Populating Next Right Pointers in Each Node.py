"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children
).
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
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..
        next = N..

c_ Solution:
    ___ connect  root):
        """
        bfs
        :param root: TreeNode
        :return: nothing
        """
        __ n.. root:
            r.. N..

        q = [root]
        w.... q:
            current_level = q
            q    # list
            ___ ind, val __ e..(current_level):
                __ val.left: q.a..(val.left)
                __ val.right: q.a..(val.right)
                ___
                    val.next = current_level[ind+1]
                ______ IndexError:
                    val.next = N..


