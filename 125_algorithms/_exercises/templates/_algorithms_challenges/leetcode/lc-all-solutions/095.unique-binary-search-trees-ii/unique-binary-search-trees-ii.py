class Solution(object):
  ___ generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """

    ___ clone(root, offset):
      __ root:
        newRoot = TreeNode(root.val + offset)
        left = clone(root.left, offset)
        right = clone(root.right, offset)
        newRoot.left = left
        newRoot.right = right
        r.. newRoot

    __ n.. n:
      r.. []
    dp = [[]] * (n + 1)
    dp[0] = [N..]
    ___ i __ r..(1, n + 1):
      dp[i]    # list
      ___ j __ r..(1, i + 1):
        ___ left __ dp[j - 1]:
          ___ right __ dp[i - j]:
            root = TreeNode(j)
            root.left = left
            root.right = clone(right, j)
            dp[i].a..(root)
    r.. dp[-1]
