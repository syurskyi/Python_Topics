# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Codec:

  ___ serialize(self, root
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    ret = []
    queue = deque([root])
    w___ queue:
      top = queue.popleft()
      __ not top:
        ret.append("None")
        continue
      ____
        ret.append(str(top.val))
      queue.append(top.left)
      queue.append(top.right)
    r_ ",".join(ret)

  ___ deserialize(self, data
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    left = lambda n: 2 * n + 1
    right = lambda n: 2 * n + 2
    data = data.split(",")
    __ data[0] __ "None":
      r_ None
    root = TreeNode(int(data[0]))
    queue = deque([root])
    i = 0
    w___ queue and i < le.(data
      top = queue.popleft()
      i += 1
      left = right = None
      __ i < le.(data) and data[i] != "None":
        left = TreeNode(int(data[i]))
        queue.append(left)
      i += 1
      __ i < le.(data) and data[i] != "None":
        right = TreeNode(int(data[i]))
        queue.append(right)

      top.left = left
      top.right = right

    r_ root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
