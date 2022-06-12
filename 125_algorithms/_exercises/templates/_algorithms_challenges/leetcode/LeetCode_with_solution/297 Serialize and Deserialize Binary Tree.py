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
____ c.. _______ d..

__author__ 'Daniel'


c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..


c_ Codec:
    ___ serialize  root
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
        ret.a..(s..(root.val  # add result when enqueue
        w.... q:
            l l..(q)
            ___ i __ x..(l
                cur q[i]
                __ cur.left: q.a..(cur.left)
                ret.a..(encode(cur.left
                __ cur.right: q.a..(cur.right)
                ret.a..(encode(cur.right

            q q[l:]

        r.. ",".j..(ret)

    ___ deserialize  data
        """
        Decodes your encoded data to tree.
        decode: 1, 2, 3, null, null, 4, 5, null, null, null, null
        :type data: str
        :rtype: TreeNode
        """
        lst ?.s..(",")
        root d.. lst 0

        q d..([root])
        i 1
        w.... q:
            cur q.popleft()
            __ i < l..(lst
                cur.left d.. lst[i])
                i += 1
                __ cur.left: q.a..(cur.left)
            __ i < l..(lst
                cur.right d.. lst[i])
                i += 1
                __ cur.right: q.a..(cur.right)

        r.. root

    ___ decode  s
        __ s __ "null":
            r.. N..
        ____
            r.. TreeNode(i..(s

    ___ encode  node
        __ n.. node:
            r.. "null"
        ____
            r.. s..(node.val)
