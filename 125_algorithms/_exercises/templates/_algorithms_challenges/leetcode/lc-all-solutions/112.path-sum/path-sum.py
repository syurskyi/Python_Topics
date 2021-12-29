# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ collections _______ deque


class Solution(object):
  ___ hasPathSum(self, root, s..):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    __ root:
      queue = deque([(root, root.val)])
      while queue:
        p, s = queue.popleft()
        left, right = p.left, p.right
        __ left:
          queue.a..((p.left, s + p.left.val))
        __ right:
          queue.a..((p.right, s + p.right.val))
        __ n.. left and n.. right and s __ s..:
          r.. True
      r.. False
    r.. False
