"""
Premium Question
"""
__author__ = 'Daniel'


c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(object):
    ___ verticalOrder(self, root):
        """
        O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = leftmost(root, 0)
        r = rightmost(root, 0)

        ret = [[] ___ _ __ xrange(r-l-1)]
        bfs(root, -l-1, ret)
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
        r.. m..(leftmost(cur.left, l-1), leftmost(cur.right, l+1))

    ___ rightmost(self, cur, r):
        __ n.. cur: r.. r
        r.. max(rightmost(cur.left, r-1), rightmost(cur.right, r+1))

    ___ sidemost(self, cur, p, f):
        __ n.. cur: r.. p
        r.. f(sidemost(cur.left, p-1, f), sidemost(cur.right, p+1, f))