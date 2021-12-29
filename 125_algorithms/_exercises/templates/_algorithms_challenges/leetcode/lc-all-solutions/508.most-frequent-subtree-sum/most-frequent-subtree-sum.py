# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ findFrequentTreeSum(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ helper(root, d):
      __ not root:
        return 0
      left = helper(root.left, d)
      right = helper(root.right, d)
      subtreeSum = left + right + root.val
      d[subtreeSum] = d.get(subtreeSum, 0) + 1
      return subtreeSum

    d = {}
    helper(root, d)
    mostFreq = 0
    ans = []
    for key in d:
      __ d[key] > mostFreq:
        mostFreq = d[key]
        ans = [key]
      elif d[key] == mostFreq:
        ans.append(key)
    return ans
