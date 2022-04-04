"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ closestKValues  root, target, k
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        """
        ans    # list

        __ n.. root:
            r.. ans

        vals    # list
        inorder_traverse(root, vals)

        n = l..(vals)
        i = 0

        w.... i < n a.. vals[i] < target:
            i += 1

        i, j = i - 1, i

        w.... k a.. i >= 0 a.. j < n:
            __ target - vals[i] < vals[j] - target:
                ans.a..(vals[i])
                i -= 1
            ____
                ans.a..(vals[j])
                j += 1
            k -= 1

        w.... k a.. i >= 0:
            ans.a..(vals[i])
            i -= 1
            k -= 1

        w.... k a.. j < n:
            ans.a..(vals[j])
            j += 1
            k -= 1

        r.. ans

    ___ inorder_traverse  root, vals
        __ n.. root:
            r..

        inorder_traverse(root.left, vals)
        vals.a..(root.val)
        inorder_traverse(root.right, vals)
