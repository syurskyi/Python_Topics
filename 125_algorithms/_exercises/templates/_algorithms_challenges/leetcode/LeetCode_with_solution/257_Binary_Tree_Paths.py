# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param {TreeNode} root
    # @return {string[]}
    ___ binaryTreePaths  root
        __ root is N..:
            r_    # list
        paths =    # list
        get_path(paths,    # list, root)
        res = ['->'.join(p) ___ p __ paths ]
        r_ res

    ___ get_path  result, path, node
        __ node.left is N.. a.. node.right is N..:
            result.a.. path + [s..(node.val)])
            r_
        path = path + [s..(node.val)]
        __ node.left is n.. N..:
            get_path(result, path, node.left)
        __ node.right is n.. N..:
            get_path(result, path, node.right)