# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Solution(object
  ___ hasPathSum(self, root, sum
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    __ root:
      queue = deque([(root, root.val)])
      w___ queue:
        p, s = queue.popleft()
        left, right = p.left, p.right
        __ left:
          queue.append((p.left, s + p.left.val))
        __ right:
          queue.append((p.right, s + p.right.val))
        __ not left and not right and s __ sum:
          r_ True
      r_ False
    r_ False
