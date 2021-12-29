"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/
deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to
follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should
be stateless.
"""
____ collections _______ deque

__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Codec:
    ___ serialize(self, root):
        """
        bfs
        Encodes a tree to a single string.

        encode to: 1, 2, 3, null, null, 4, 5, null, null, null, null
        :type root: TreeNode
        :rtype: str
        """
        __ n.. root:
            r.. "null"

        ret    # list
        q    # list
        q.a..(root)
        ret.a..(str(root.val))  # add result when enqueue
        while q:
            l = l..(q)
            ___ i __ xrange(l):
                cur = q[i]
                __ cur.left: q.a..(cur.left)
                ret.a..(self.encode(cur.left))
                __ cur.right: q.a..(cur.right)
                ret.a..(self.encode(cur.right))

            q = q[l:]

        r.. ",".join(ret)

    ___ deserialize(self, data):
        """
        Decodes your encoded data to tree.
        decode: 1, 2, 3, null, null, 4, 5, null, null, null, null
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")
        root = self.decode(lst[0])

        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            __ i < l..(lst):
                cur.left = self.decode(lst[i])
                i += 1
                __ cur.left: q.a..(cur.left)
            __ i < l..(lst):
                cur.right = self.decode(lst[i])
                i += 1
                __ cur.right: q.a..(cur.right)

        r.. root

    ___ decode(self, s):
        __ s __ "null":
            r.. N..
        ____:
            r.. TreeNode(int(s))

    ___ encode(self, node):
        __ n.. node:
            r.. "null"
        ____:
            r.. str(node.val)
