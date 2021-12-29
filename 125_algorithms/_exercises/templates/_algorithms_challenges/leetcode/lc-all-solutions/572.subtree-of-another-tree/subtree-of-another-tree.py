# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    ___ serialize(root):
      ans = []
      stack = [(root, 1)]
      while stack:
        node, p = stack.pop()
        __ not node:
          ans.append("#")
          continue
        __ p == 0:
          ans.append("|" + str(node.val))
        else:
          stack.append((node.right, 1))
          stack.append((node.left, 1))
          stack.append((node, 0))
      return ",".join(ans)

    return serialize(t) in serialize(s)
