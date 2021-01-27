# Definition for a binary tree node.
class TreeNode:
    ___  -   val=0, left=N.., right=N..):
        val = val
        left = left
        right = right


class Solution:
    ___ buildTree  preorder, inorder):
        memory = {}
        ___ i, e __ enumerate(inorder):
            memory[e] = i

        root = helper(preorder[::-1], inorder, 0, le.(inorder), memory)
        r_ root

    ___ helper  preorder, inorder, leftPointer, rightPointer, memory):
        __ leftPointer >= rightPointer:
            r_ N..

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)

        root.left = helper(preorder, inorder, leftPointer, idx, memory)
        root.right = helper(preorder, inorder, idx + 1, rightPointer, memory)

        r_ root