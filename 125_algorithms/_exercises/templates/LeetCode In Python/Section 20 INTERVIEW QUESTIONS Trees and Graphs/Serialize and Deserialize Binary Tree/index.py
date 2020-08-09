# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


c_ Codec:

    ___ serialize(, root
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        __(root is None
            r_ "X#"

        leftSerialized _ .serialize(root.left)
        rightSerialized _ .serialize(root.right)

        r_ st.(root.val)+"#"+leftSerialized+rightSerialized

    ___ deserialize(, data
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        ___ dfs(
            val _ next(data)
            __ val __ 'X':
                r_ None
            node _ TreeNode(in.(val))

            node.left _ dfs()
            node.right _ dfs()

            r_ node

        data _ iter(data.split("#"))
        r_ dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
