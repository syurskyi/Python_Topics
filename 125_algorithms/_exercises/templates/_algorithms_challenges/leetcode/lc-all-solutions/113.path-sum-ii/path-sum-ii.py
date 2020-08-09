# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ pathSum(self, root, sum
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    ___ dfs(root, s, path, res
      __ root:
        path.append(root.val)
        s -= root.val
        left = dfs(root.left, s, path, res)
        right = dfs(root.right, s, path, res)
        __ not left and not right and s __ 0:
          res.append(path + [])
        path.pop()
        r_ True

    res = []
    dfs(root, sum, [], res)
    r_ res
