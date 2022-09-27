# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # https://leetcode.com/problems/subtree-of-another-tree/solution/
    ___ isSubtree  s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_res = preorder(s, T..)
        t_res = preorder(t, T..)
        r_ t_res __ s_res
    
    ___ preorder  root, isLeft):
        __ root is N..:
            __ isLeft:
                r_ "lnull"
            ____
                r_ "rnull"
        r_ "#" + s..(root.val) + " " + preorder(root.left, T..) + " " + preorder(root.right, F..)

    # def isSubtree(self, s, t):
    #     return self.traverse(s, t)
    
    # def equals(self, x, y):
    #     if x is None and y is None:
    #         return True
    #     if x is None or y is None:
    #         return False
    #     return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)
    
    # def traverse(self, s, t):
    #     return s is not None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
