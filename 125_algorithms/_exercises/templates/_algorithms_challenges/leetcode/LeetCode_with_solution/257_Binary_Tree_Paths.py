# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param {TreeNode} root
    # @return {string[]}
    ___ binaryTreePaths  root):
        __ root is N..:
            r_ []
        paths = []
        get_path(paths, [], root)
        res = ['->'.join(p) ___ p __ paths ]
        r_ res

    ___ get_path  result, path, node):
        __ node.left is N.. and node.right is N..:
            result.append(path + [str(node.val)])
            r_
        path = path + [str(node.val)]
        __ node.left is not N..:
            get_path(result, path, node.left)
        __ node.right is not N..:
            get_path(result, path, node.right)