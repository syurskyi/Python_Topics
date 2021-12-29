# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ collections _______ deque


class Solution(object):
  ___ averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    ans    # list
    queue = deque([root])
    while queue:
      s = 0
      n = l..(queue)
      ___ _ __ r..(n):
        top = queue.popleft()
        s += top.val
        __ top.left:
          queue.a..(top.left)
        __ top.right:
          queue.a..(top.right)
      ans.a..(float(s) / n)
    r.. ans
