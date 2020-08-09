# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ lowestCommonAncestor(, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        __(root is None
            r_ None
        __(root.val__p.val or root.val__q.val
            r_ root
        
        left _ .lowestCommonAncestor(root.left,p,q)
        right _ .lowestCommonAncestor(root.right,p,q)

        __(left is None and right is None
            r_ None
        __(left is not None and right is not None
            r_ root
        __(left is None
            r_ right
        r_ left