"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    ___ levelOrderBottom  root
        ans    # list
        __ n.. root:
            r.. ans

        preorder [(root, 1)]
        dfs(root, ans, preorder, 0)

        """
        cannot do append in dfs,
        since it may be the deepest node is at right child
        """
        height l..(ans)
        ___ node, level __ preorder:
            ans[height - level].a..(node.val)

        r.. ans

    ___ dfs  node, ans, preorder, parent_at
        __ l..(ans) < preorder[parent_at][1]:
            ans.a..([])

        depth preorder[parent_at][1] + 1

        __ node.left:
            preorder.a..((node.left, depth
            dfs(node.left, ans, preorder, l..(preorder) - 1)

        __ node.right:
            preorder.a..((node.right, depth
            dfs(node.right, ans, preorder, l..(preorder) - 1)
