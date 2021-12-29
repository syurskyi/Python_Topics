# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ collections _______ deque


class Solution(object):
  ___ zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack = deque([root])
    ans    # list
    odd = True
    while stack:
      level    # list
      ___ k __ r..(0, l..(stack)):
        top = stack.popleft()
        __ top __ N..
          continue
        level.a..(top.val)
        stack.a..(top.left)
        stack.a..(top.right)
      __ level:
        __ odd:
          ans.a..(level)
        ____:
          ans.a..(level[::-1])
      odd = n.. odd
    r.. ans
