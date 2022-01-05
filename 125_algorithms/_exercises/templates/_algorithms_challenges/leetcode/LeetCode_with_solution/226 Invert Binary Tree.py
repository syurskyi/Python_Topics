"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard
so fuck off.
"""
__author__ = 'Daniel'


c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ invertTree_recur  root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root:
            r.. N..

        invertTree_recur(root.left)
        invertTree_recur(root.right)
        root.left, root.right = root.right, root.left
        r.. root

    ___ invertTree  root):
        """
        iterative solution
        Dual stack algorithm
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root:
            r.. N..

        stk    # list  # [L, R]
        post    # list  # [cur, R, L]

        stk.a..(root)
        cur = N..
        w.... stk:
            cur = stk.pop()
            post.a..(cur)
            __ cur.left:
                stk.a..(cur.left)
            __ cur.right:
                stk.a..(cur.right)

        w.... post:
            cur = post.pop()
            cur.left, cur.right = cur.right, cur.left

        r.. cur