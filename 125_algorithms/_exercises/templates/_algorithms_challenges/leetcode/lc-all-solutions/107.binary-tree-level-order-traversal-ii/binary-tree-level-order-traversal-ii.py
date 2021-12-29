# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ collections _______ deque


class Solution(object):
  ___ levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    __ n.. root:
      r.. []
    ans = [[root.val]]
    queue = deque([root])
    w.... queue:
      levelans    # list
      ___ _ __ r..(0, l..(queue)):
        root = queue.popleft()
        __ root.left:
          levelans.a..(root.left.val)
          queue.a..(root.left)
        __ root.right:
          levelans.a..(root.right.val)
          queue.a..(root.right)
      __ levelans:
        ans.a..(levelans)
    r.. ans[::-1]
