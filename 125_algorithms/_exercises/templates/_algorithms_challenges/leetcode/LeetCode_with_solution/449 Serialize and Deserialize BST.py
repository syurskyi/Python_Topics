"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is
no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


# Definition for a binary tree node.
c_ TreeNode(o..
  ___ - , x
      val = x
      left = N..
      right = N..


c_ Codec:
    DELIMITER = ","

    ___ serialize  root
        """Encodes a tree to a single string.
        Basic binary tree serialize (BFS), see Serialize and Deserialize
        Binary Tree

        The main difference is as compact as possible. No need "null", since
        insertion order is specfied.

            3 (1)
        2 (2)  5 (2)
                 6 (3)  # bracket () is the insertion order

        pre-order traversal keeps the insertion order
        :type root: TreeNode
        :rtype: str
        """
        ___ traverse(root, ret
            __ n.. root:
                r..

            ret.a..(root.val)
            traverse(root.left, ret)
            traverse(root.right, ret)

        ret    # list
        traverse(root, ret)
        r.. DELIMITER.j.. m..(s.., ret

    ___ deserialize  data
        """Decodes your encoded data to tree.

        Normal BST insert
        :type data: str
        :rtype: TreeNode
        """
        __ n.. data:
            r..
            
        lst = l.. m..(i.., data.s..(DELIMITER)))
        root = TreeNode(lst[0])
        ___ insert(root, val
            # need to keep the parent
            __ val < root.val:
                __ n.. root.left:
                    root.left = TreeNode(val)
                ____:
                    insert(root.left, val)
            ____:
                __ n.. root.right:
                    root.right = TreeNode(val)
                ____:
                    insert(root.right, val)

        ___ a __ lst[1:]:
            insert(root, a)

        r.. root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
