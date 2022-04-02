# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ findMode  root
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ visit(v
      __ v != pre:
        pre = v
        cnt = 0
      cnt += 1
      __ cnt > maxFreq:
        maxFreq = cnt
        modeCnt = 1
      ____ cnt __ maxFreq:
        __ ans:
          ans[modeCnt] = v
        modeCnt += 1

    ___ inorder(root
      __ root:
        inorder(root.left)
        visit(root.val)
        inorder(root.right)

    pre = N..
    ans = N..
    maxFreq = modeCnt = cnt = 0
    inorder(root)
    ans = [0] * modeCnt
    modeCnt = cnt = 0
    inorder(root)
    r.. ans
