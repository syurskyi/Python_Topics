class Solution(object
  ___ generateTrees(self, n
    """
    :type n: int
    :rtype: List[TreeNode]
    """

    ___ clone(root, offset
      __ root:
        newRoot = TreeNode(root.val + offset)
        left = clone(root.left, offset)
        right = clone(root.right, offset)
        newRoot.left = left
        newRoot.right = right
        r_ newRoot

    __ not n:
      r_ []
    dp = [[]] * (n + 1)
    dp[0] = [None]
    for i in range(1, n + 1
      dp[i] = []
      for j in range(1, i + 1
        for left in dp[j - 1]:
          for right in dp[i - j]:
            root = TreeNode(j)
            root.left = left
            root.right = clone(right, j)
            dp[i].append(root)
    r_ dp[-1]
