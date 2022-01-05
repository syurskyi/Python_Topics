"""
Premium Question
Recursive
Longest Consecutive Subsequence in BT
"""
__author__ = 'Daniel'


c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(o..):
    ___ - ):
        gmax = 0

    ___ longestConsecutive  root):
        longest(root)
        r.. gmax

    ___ longest  cur):
        """
        longest ended at root
        Only consider increasing order
        """
        __ n.. cur:
            r.. 0

        maxa = 1
        l = longest(cur.left)
        r = longest(cur.right)
        __ cur.left a.. cur.val+1 __ cur.left.val:
            maxa = m..(maxa, l+1)
        __ cur.right a.. cur.val+1 __ cur.right.val:
            maxa = m..(maxa, r+1)

        gmax = m..(gmax, maxa)
        r.. maxa

    ___ longestConsecutive_error  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        maxa = 1
        l = longestConsecutive(root.left)
        r = longestConsecutive(root.right)
        maxa = m..(maxa, l, r)
        __ root.left a.. root.val + 1 __ root.left.val:
            maxa = m..(maxa, l+1)
        __ root.right a.. root.val + 1 __ root.right.val:
            maxa = m..(maxa, r+1)

        r.. maxa