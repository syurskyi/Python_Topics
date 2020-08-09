# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    ___ serialize(self, root
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        __(root is None
            r_ "X#"

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        r_ str(root.val)+"#"+leftSerialized+rightSerialized

    ___ deserialize(self, data
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        ___ dfs(
            val = next(data)
            __ val __ 'X':
                r_ None
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            r_ node

        data = iter(data.split("#"))
        r_ dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
