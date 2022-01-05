# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..):
  ___ findFrequentTreeSum  root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ helper(root, d):
      __ n.. root:
        r.. 0
      left = helper(root.left, d)
      right = helper(root.right, d)
      subtreeSum = left + right + root.val
      d[subtreeSum] = d.get(subtreeSum, 0) + 1
      r.. subtreeSum

    d    # dict
    helper(root, d)
    mostFreq = 0
    ans    # list
    ___ key __ d:
      __ d[key] > mostFreq:
        mostFreq = d[key]
        ans = [key]
      ____ d[key] __ mostFreq:
        ans.a..(key)
    r.. ans
