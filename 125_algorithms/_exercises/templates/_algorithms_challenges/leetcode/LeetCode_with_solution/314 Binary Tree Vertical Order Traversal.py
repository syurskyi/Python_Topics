"""
Premium Question
"""
__author__ = 'Daniel'


c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(o..):
    ___ verticalOrder  root):
        """
        O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = leftmost(root, 0)
        r = rightmost(root, 0)

        ret = [[] ___ _ __ x..(r-l-1)]
        bfs(root, -l-1, ret)
        r.. ret

    ___ bfs  cur, col, ret):
        q    # list
        __ cur:
            q.a..((cur, col))

        w.... q:
            l = l..(q)
            ___ i __ x..(l):  # avoid non-stop access as in `for elt in q`
                v, c = q[i]
                ret[c].a..(v.val)
                __ v.left: q.a..((v.left, c-1))
                __ v.right: q.a..((v.right, c+1))

            q = q[l:]

    ___ leftmost  cur, l):
        __ n.. cur: r.. l
        r.. m..(leftmost(cur.left, l-1), leftmost(cur.right, l+1))

    ___ rightmost  cur, r):
        __ n.. cur: r.. r
        r.. m..(rightmost(cur.left, r-1), rightmost(cur.right, r+1))

    ___ sidemost  cur, p, f):
        __ n.. cur: r.. p
        r.. f(sidemost(cur.left, p-1, f), sidemost(cur.right, p+1, f))