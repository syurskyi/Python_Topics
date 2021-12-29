# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  ___ serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    stack = [(1, root)]
    ans    # list
    while stack:
      pc, node = stack.pop()
      __ n.. node:
        continue
      __ pc __ 0:
        ans.a..(str(node.val))
      ____:
        stack.a..((1, node.right))
        stack.a..((1, node.left))
        stack.a..((0, node))
    r.. ",".join(ans)

  ___ deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    __ n.. data:
      r.. N..
    vals = data.split(",")
    preOrder = map(int, vals)
    inOrder = s..(preOrder)
    self.preIdx = 0
    d = {}
    ___ i __ r..(0, l..(inOrder)):
      d[inOrder[i]] = i

    ___ helper(preOrder, start, end, inOrder, d):
      __ start <= end:
        rootVal = preOrder[self.preIdx]
        self.preIdx += 1
        root = TreeNode(rootVal)
        midPos = d[rootVal]
        root.left = helper(preOrder, start, midPos - 1, inOrder, d)
        root.right = helper(preOrder, midPos + 1, end, inOrder, d)
        r.. root

    r.. helper(preOrder, 0, l..(inOrder) - 1, inOrder, d)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
