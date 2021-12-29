"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ verticalOrder(self, root):
        """
        O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = self.leftmost(root, 0)
        r = self.rightmost(root, 0)

        ret = [[] ___ _ __ xrange(r-l-1)]
        self.bfs(root, -l-1, ret)
        r.. ret

    ___ bfs(self, cur, col, ret):
        q    # list
        __ cur:
            q.a..((cur, col))

        w.... q:
            l = l..(q)
            ___ i __ xrange(l):  # avoid non-stop access as in `for elt in q`
                v, c = q[i]
                ret[c].a..(v.val)
                __ v.left: q.a..((v.left, c-1))
                __ v.right: q.a..((v.right, c+1))

            q = q[l:]

    ___ leftmost(self, cur, l):
        __ n.. cur: r.. l
        r.. m..(self.leftmost(cur.left, l-1), self.leftmost(cur.right, l+1))

    ___ rightmost(self, cur, r):
        __ n.. cur: r.. r
        r.. max(self.rightmost(cur.left, r-1), self.rightmost(cur.right, r+1))

    ___ sidemost(self, cur, p, f):
        __ n.. cur: r.. p
        r.. f(self.sidemost(cur.left, p-1, f), self.sidemost(cur.right, p+1, f))