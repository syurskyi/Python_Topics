"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution(object
    ___ verticalOrder(self, root
        """
        O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = self.leftmost(root, 0)
        r = self.rightmost(root, 0)

        ret = [[] for _ in xrange(r-l-1)]
        self.bfs(root, -l-1, ret)
        r_ ret

    ___ bfs(self, cur, col, ret
        q = []
        __ cur:
            q.append((cur, col))

        w___ q:
            l = le.(q)
            for i in xrange(l  # avoid non-stop access as in `for elt in q`
                v, c = q[i]
                ret[c].append(v.val)
                __ v.left: q.append((v.left, c-1))
                __ v.right: q.append((v.right, c+1))

            q = q[l:]

    ___ leftmost(self, cur, l
        __ not cur: r_ l
        r_ min(self.leftmost(cur.left, l-1), self.leftmost(cur.right, l+1))

    ___ rightmost(self, cur, r
        __ not cur: r_ r
        r_ max(self.rightmost(cur.left, r-1), self.rightmost(cur.right, r+1))

    ___ sidemost(self, cur, p, f
        __ not cur: r_ p
        r_ f(self.sidemost(cur.left, p-1, f), self.sidemost(cur.right, p+1, f))