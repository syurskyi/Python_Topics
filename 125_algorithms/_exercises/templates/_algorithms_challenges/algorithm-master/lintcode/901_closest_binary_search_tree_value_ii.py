"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ closestKValues(self, root, target, k
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        """
        ans = []

        __ not root:
            r_ ans

        vals = []
        self.inorder_traverse(root, vals)

        n = le.(vals)
        i = 0

        w___ i < n and vals[i] < target:
            i += 1

        i, j = i - 1, i

        w___ k and i >= 0 and j < n:
            __ target - vals[i] < vals[j] - target:
                ans.append(vals[i])
                i -= 1
            ____
                ans.append(vals[j])
                j += 1
            k -= 1

        w___ k and i >= 0:
            ans.append(vals[i])
            i -= 1
            k -= 1

        w___ k and j < n:
            ans.append(vals[j])
            j += 1
            k -= 1

        r_ ans

    ___ inorder_traverse(self, root, vals
        __ not root:
            r_

        self.inorder_traverse(root.left, vals)
        vals.append(root.val)
        self.inorder_traverse(root.right, vals)
