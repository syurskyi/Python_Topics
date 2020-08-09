"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    ___ levelOrderBottom(self, root
        ans = []
        __ not root:
            r_ ans

        preorder = [(root, 1)]
        self.dfs(root, ans, preorder, 0)

        """
        cannot do append in dfs,
        since it may be the deepest node is at right child
        """
        height = le.(ans)
        ___ node, level in preorder:
            ans[height - level].append(node.val)

        r_ ans

    ___ dfs(self, node, ans, preorder, parent_at
        __ le.(ans) < preorder[parent_at][1]:
            ans.append([])

        depth = preorder[parent_at][1] + 1

        __ node.left:
            preorder.append((node.left, depth))
            self.dfs(node.left, ans, preorder, le.(preorder) - 1)

        __ node.right:
            preorder.append((node.right, depth))
            self.dfs(node.right, ans, preorder, le.(preorder) - 1)
