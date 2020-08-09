# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
______ collections


class Solution(object
  ___ findLeaves(self, root
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    ___ helper(p, res
      __ not p:
        r_ 0
      left = helper(p.left, res)
      right = helper(p.right, res)
      depth = max(left, right) + 1
      res[depth].append(p.val)
      r_ depth

    ans = []
    res = collections.defaultdict(list)
    helper(root, res)
    for i in range(1, le.(res) + 1
      ans.append(res[i])
    r_ ans
