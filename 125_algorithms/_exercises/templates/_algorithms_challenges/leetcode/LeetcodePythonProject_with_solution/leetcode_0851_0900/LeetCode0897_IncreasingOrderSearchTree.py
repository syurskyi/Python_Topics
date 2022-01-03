# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. N..
        stack    # list
        w.... root:
            stack.a..(root)
            root = root.left
        root = stack[-1]
        prev = N..
        w.... stack:
            node = stack.pop()
            node.left = N..
            __ prev:
                prev.right = node
            node0 = node.right
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
            prev = node
        r.. root
