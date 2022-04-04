# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ c.. _______ d..


c_ Solution(o..
  ___ hasPathSum  root, s..
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    __ root:
      queue = d..([(root, root.val)])
      w.... queue:
        p, s = queue.popleft()
        left, right = p.left, p.right
        __ left:
          queue.a..((p.left, s + p.left.val
        __ right:
          queue.a..((p.right, s + p.right.val
        __ n.. left a.. n.. right a.. s __ s..:
          r.. T..
      r.. F..
    r.. F..
