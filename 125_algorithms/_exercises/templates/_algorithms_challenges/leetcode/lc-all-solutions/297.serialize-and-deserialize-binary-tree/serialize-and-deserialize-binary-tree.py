# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ c.. _______ d..


c_ Codec:

  ___ serialize  root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    ret    # list
    queue = d..([root])
    w.... queue:
      top = queue.popleft()
      __ n.. top:
        ret.a..("None")
        _____
      ____:
        ret.a..(s..(top.val))
      queue.a..(top.left)
      queue.a..(top.right)
    r.. ",".j..(ret)

  ___ deserialize  data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    left = l.... n: 2 * n + 1
    right = l.... n: 2 * n + 2
    data = data.s..(",")
    __ data[0] __ "None":
      r.. N..
    root = TreeNode(i..(data[0]))
    queue = d..([root])
    i = 0
    w.... queue a.. i < l..(data):
      top = queue.popleft()
      i += 1
      left = right = N..
      __ i < l..(data) a.. data[i] != "None":
        left = TreeNode(i..(data[i]))
        queue.a..(left)
      i += 1
      __ i < l..(data) a.. data[i] != "None":
        right = TreeNode(i..(data[i]))
        queue.a..(right)

      top.left = left
      top.right = right

    r.. root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
