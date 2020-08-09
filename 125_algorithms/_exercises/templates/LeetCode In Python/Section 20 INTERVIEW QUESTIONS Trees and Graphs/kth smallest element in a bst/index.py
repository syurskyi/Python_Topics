class Solution:
    ___ kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root)
        r_ self.res

    ___ helper(self, root
        __ not root:
            r_
        self.helper(root.left)
        
        self.k -= 1
        __ self.k __ 0:
            self.res = root.val
            r_
        self.helper(root.right)
