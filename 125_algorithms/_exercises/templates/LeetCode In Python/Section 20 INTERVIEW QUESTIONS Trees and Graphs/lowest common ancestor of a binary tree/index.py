# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ lowestCommonAncestor root: 'TreeNode', p: 'TreeNode', q: 'TreeNode')  'TreeNode':
        __(root pa__ N..
            r_ N..
        __(root.val__p.val o.. root.val__q.val
            r_ root
        
        left _ .lowestCommonAncestor(root.left,p,q)
        right _ .lowestCommonAncestor(root.right,p,q)

        __(left pa__ N.. a.. right pa__ N..
            r_ N..
        __(left pa__ no. N.. a.. right pa__ no. N..
            r_ root
        __(left pa__ N..
            r_ right
        r_ left