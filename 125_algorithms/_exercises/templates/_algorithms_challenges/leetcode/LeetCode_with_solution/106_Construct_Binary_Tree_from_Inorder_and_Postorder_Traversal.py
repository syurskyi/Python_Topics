# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ buildTree  inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = l.. inorder)
        inOrderMap = {inorder[i]: i ___ i __ r.. n)}
        r_ buildTreeUtil(inorder, postorder, inOrderMap, 0, n - 1, 0, n - 1)

    ___ buildTreeUtil  inorder, postorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        __ pStart > pEnd or iStart > iEnd:
            r_ N..

        root = TreeNode(postorder[pEnd])
        rootIdx = inOrderMap[root.val]
        root.left = buildTreeUtil(inorder, postorder, inOrderMap, pStart, pStart + rootIdx - iStart - 1, iStart,
                                       rootIdx - 1)
        root.right = buildTreeUtil(inorder, postorder, inOrderMap, pStart + rootIdx - iStart, pEnd - 1, rootIdx + 1,
                                        iEnd)
        r_ root

