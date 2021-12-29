# # Definition for a binary tree node.
# # class TreeNode(object
# #     ___ __init__(self, x
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
#
# c_ Codec
#
#     ___ serialize root
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         __ ? pa__ N..
#             r_ "X#"
#
#         leftSerialized _ .? ?.l..
#         rightSerialized _ .? ?.r..
#
#         r_ st. ?.v.. +"#"+?+?
#
#     ___ deserialize data
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#
#         ___ dfs
#             val _ n.. data
#             __ ? __ 'X'
#                 r_ N..
#             node _ TN.. in. ?
#
#             ?.l.. _ ?
#             ?.r.. _ ?
#
#             r_ ?
#
#         data _ it.. ?.sp.. "#"
#         r_ ?
#
#
# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.deserialize(codec.serialize(root))
