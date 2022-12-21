# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """
    #     # https://leetcode.com/discuss/102884/c-12ms-iterative-solution
    #     if preorder is None or len(preorder) == 0:
    #         return None
    #     root = TreeNode(preorder[0])
    #     pre = root
    #     stack = [root]
    #     flag, pp, pi = 0, 1, 0
    #     while pi < len(inorder):
    #         if len(stack) > 0 and stack[-1].val == inorder[pi]:
    #             pre = stack[-1]
    #             flag = 1
    #             stack.pop()
    #             pi += 1
    #         else:
    #             temp = TreeNode(preorder[pp])
    #             if flag == 0:
    #                 pre.left = temp
    #                 pre = pre.left
    #             else:
    #                 pre.right = temp
    #                 pre = pre.right
    #                 flag = 0
    #             stack.append(temp)
    #             pp += 1
    #     return root


    ___ buildTree  preorder, inorder
        n = l.. inorder)
        inOrderMap = {inorder[i]: i ___ i __ r.. n)}
        r_ buildTreeUtil(preorder, inorder, inOrderMap, 0, n - 1, 0, n - 1)

    ___ buildTreeUtil  preorder, inorder, inOrderMap, pStart, pEnd, iStart, iEnd
        __ pStart > pEnd or iStart > iEnd:
            r_ N..
        root = TreeNode(preorder[pStart])
        rootIdx = inOrderMap[root.val]
        root.left = buildTreeUtil(preorder, inorder, inOrderMap, pStart + 1, pStart + rootIdx - iStart + 1, iStart,
                                       rootIdx - 1)
        root.right = buildTreeUtil(preorder, inorder, inOrderMap, pStart + rootIdx - iStart + 1, pEnd, rootIdx + 1,
                                        iEnd)
        r_ root



    # def buildTree(self, preorder, inorder):
    # basic idea but memory not enough
    #     if preorder is None or len(preorder) == 0:
    #         return None
    #     root = TreeNode(preorder[0])
    #     root_index = inorder.index(root.val)
    #     root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
    #     root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
    #     return root
