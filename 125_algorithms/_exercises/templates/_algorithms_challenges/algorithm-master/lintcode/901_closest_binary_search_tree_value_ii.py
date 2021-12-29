"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        """
        ans    # list

        __ n.. root:
            r.. ans

        vals    # list
        self.inorder_traverse(root, vals)

        n = l..(vals)
        i = 0

        while i < n and vals[i] < target:
            i += 1

        i, j = i - 1, i

        while k and i >= 0 and j < n:
            __ target - vals[i] < vals[j] - target:
                ans.a..(vals[i])
                i -= 1
            ____:
                ans.a..(vals[j])
                j += 1
            k -= 1

        while k and i >= 0:
            ans.a..(vals[i])
            i -= 1
            k -= 1

        while k and j < n:
            ans.a..(vals[j])
            j += 1
            k -= 1

        r.. ans

    ___ inorder_traverse(self, root, vals):
        __ n.. root:
            r..

        self.inorder_traverse(root.left, vals)
        vals.a..(root.val)
        self.inorder_traverse(root.right, vals)
