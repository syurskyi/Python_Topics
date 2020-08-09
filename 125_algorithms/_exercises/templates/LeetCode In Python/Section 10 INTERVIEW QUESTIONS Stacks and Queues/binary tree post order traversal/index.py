# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ postorderTraversal(, root: TreeNode) -> L.. in.:
        __(no. root
            r_
        
        ans _ []
        s1 _ []
        s2 _ []

        s1.ap..(root)

        w___(s1
            x _ s1[-1]
            s1.pop()
            s2.ap..(x)

            __(x.left
                s1.ap..(x.left)
            __(x.right
                s1.ap..(x.right)
        
        w___(s2
            y _ s2[-1]
            s2.pop()
            ans.ap..(y.val)
        r_ ans